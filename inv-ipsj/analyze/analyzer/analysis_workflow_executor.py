from typing import List
import json

from .analysis_strategy import analyze_timet_to_int, analyze_timet_to_long, analyze_read_fs_timestamp, analyze_write_fs_timestamp
from domain.analysis import Analysis
from domain.analysis_detail import AnalysisDetail
from domain.timer import Timer


class AnalysisWorkflowExecutor():
    def __init__(self, name: str, compile_json_path: str) -> None:
        self.compile_json_path = compile_json_path
        self.analysis = Analysis(
            name=name,
            count_files=self._count_files(compile_json_path)
        )
        self.analysis_detail_list: List[AnalysisDetail] = []

    def _analyze(self, compile_json_path: str, analysis_id: str) -> List[AnalysisDetail]:
        analysis_detail_list: List[AnalysisDetail] = []
        # 高速化のため .extend() を使う
        analysis_detail_list.extend(analyze_timet_to_int(compile_json_path, analysis_id))
        analysis_detail_list.extend(analyze_timet_to_long(compile_json_path, analysis_id))
        analysis_detail_list.extend(analyze_read_fs_timestamp(compile_json_path, analysis_id))
        analysis_detail_list.extend(analyze_write_fs_timestamp(compile_json_path, analysis_id))
        return analysis_detail_list

    def _count_files(self, compile_json_path: str) -> int:
        with open(compile_json_path, 'r') as file:
            json_list = json.load(file)
        return len(json_list)

    def run(self):
        # 時刻の計測開始
        timer = Timer()
        timer.start()

        # 解析を実行
        self.analysis_detail_list = self._analyze(
            compile_json_path=self.compile_json_path,
            analysis_id=self.analysis.get_id()
        )

        timer.stop()
        self.analysis.set_processing_time(timer.get_time())

    def get_analysis(self) -> Analysis:
        return self.analysis

    def get_analysis_detail_list(self) -> List[AnalysisDetail]:
        return self.analysis_detail_list


if __name__ == '__main__':
    analyzer = AnalysisWorkflowExecutor()

    analyzer.run(
        "torvalds/linux",
        compile_json_path="/home/cysec/develop/.y2k38-checker/analysis-objects/torvalds__linux/compile_commands.json"
    )

    print(analyzer.get_analysis())
    print(analyzer.get_analysis_detail_list())
