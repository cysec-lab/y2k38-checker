from typing import Literal
import os

from domain.value.file import File


Y2k38Category = Literal["read-fs-timestamp", "write-fs-timestamp", "timet-to-int-downcast", "timet-to-long-downcast"]


class AnalysisDetail():
    def __init__(self, y2k38_category: Y2k38Category, file: File, row: int, column: int) -> None:
        self.y2k38_category: Y2k38Category = y2k38_category
        self.file: File = file
        self.row: int = row
        self.column: int = column

    def get_y2k38_category(self) -> Y2k38Category:
        return self.y2k38_category

    def get_file(self) -> File:
        return self.file

    def get_row(self) -> int:
        return self.row

    def get_column(self) -> int:
        return self.column
