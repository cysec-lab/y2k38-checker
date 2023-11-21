from typing import List, Union

from .analysis_strategy import ReadFsTimestampStrategy, WriteFsTimestampStrategy, TimetToIntDowncastStrategy, TimetToLongDowncastStrategy, AnalysisContext
from domain.analysis import Analysis
from domain.analysis_detail import AnalysisDetail
from domain.timer import Timer


class AnalysisWorkflowExecutor():
    def __init__(self) -> None:
        self.analysis = None
        self.analysis_detail_list: List[AnalysisDetail] = []

    def __analyze(self, compile_json_path: str, analysis_id: str) -> List[AnalysisDetail]:
        contexts = [
            AnalysisContext(ReadFsTimestampStrategy()),
            AnalysisContext(WriteFsTimestampStrategy()),
            AnalysisContext(TimetToIntDowncastStrategy()),
            AnalysisContext(TimetToLongDowncastStrategy())
        ]
        return [
            analysis_detail
            for context in contexts
            for analysis_detail in context.operation(compile_json_path=compile_json_path, analysis_id=analysis_id)
        ]

    def run(self, name: str, compile_json_path: str):
        self.analysis = Analysis(name)

        # 時刻の計測開始
        timer = Timer()
        timer.start()

        # 解析を実行
        self.analysis_detail_list = self.__analyze(compile_json_path=compile_json_path, analysis_id=self.analysis.get_id())

        timer.stop()
        self.analysis.set_processing_time(timer.get_time())

    def get_analysis(self) -> Union[None, Analysis]:
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
