from typing import Literal

from .analysis import Analysis


class AnalysisDetail():
    AnalysisId = Analysis.Id
    Y2k38Category = Literal["read-fs-timestamp", "write-fs-timestamp", "timet-to-int-downcast", "timet-to-long-downcast"]
    Path = str

    def __init__(self, analysis_id: AnalysisId, y2k38_category: Y2k38Category, path: Path) -> None:
        self.analysis_id: AnalysisDetail.AnalysisId = analysis_id
        self.y2k38_category: AnalysisDetail.Y2k38Category = y2k38_category
        self.path: AnalysisDetail.Path = path

    def get_analysis_id(self) -> AnalysisId:
        return self.analysis_id

    def get_y2k38_category(self) -> Y2k38Category:
        return self.y2k38_category

    def get_path(self) -> str:
        return self.path
