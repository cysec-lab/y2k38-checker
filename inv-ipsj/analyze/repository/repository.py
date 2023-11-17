from typing import List

from ..domain.analysis import Analysis
from ..domain.analysis_detail import AnalysisDetail


class AnalysisRepository():
    def __init__(self) -> None:
        self.analysis_list: List[Analysis] = []

    def insert(self, analysis: Analysis):
        self.analysis_list.append(analysis)

    def write_out(self, path: str):
        with open(path, 'a') as f:
            for analysis in self.analysis_list:
                f.write(
                    f"{analysis.get_id()},{analysis.get_name()},{analysis.get_date()},{analysis.get_processing_time()}\n"
                )


class AnalysisDetailRepository():
    def __init__(self) -> None:
        self.analysis_detail_list: List[AnalysisDetail] = []

    def bulk_insert(self, analysis_detail_list: List[AnalysisDetail]):
        self.analysis_detail_list.extend(analysis_detail_list)

    def write_out(self, path: str):
        with open(path, 'a') as f:
            for analysis_detail in self.analysis_detail_list:
                f.write(
                    f"{analysis_detail.get_analysis_id()},{analysis_detail.get_y2k38_category()},{analysis_detail.get_path()}\n"
                )
