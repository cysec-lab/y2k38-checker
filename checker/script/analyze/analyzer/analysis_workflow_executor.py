from typing import List

from analyzer.clang_static_analyzer import run_clang
from analyzer.timer import Timer
from domain.analysis import Analysis
from domain.analysis_detail import AnalysisDetail
from domain.value.file import File


class AnalysisWorkflowExecutor():
    def __init__(self, files: List[File]) -> None:
        self.file = files
        self.analysis = Analysis(count_files=len(files))
        self.analysis_detail_list: List[AnalysisDetail] = []

    def __analyze(self) -> List[AnalysisDetail]:
        analysis_detail_list: List[AnalysisDetail] = []
        for file in self.file:
            analysis_detail_list.extend(run_clang(file))
        return analysis_detail_list

    def run(self):
        timer = Timer()
        timer.start()

        self.analysis_detail_list = self.__analyze()

        timer.stop()
        self.analysis.set_processing_time(timer.get_time())

    def get_analysis(self) -> Analysis:
        return self.analysis

    def get_analysis_detail_list(self) -> List[AnalysisDetail]:
        return self.analysis_detail_list


if __name__ == '__main__':
    analyzer = AnalysisWorkflowExecutor([File("path/to/file")])

    analyzer.run()

    print(analyzer.get_analysis())
    print(analyzer.get_analysis_detail_list())
