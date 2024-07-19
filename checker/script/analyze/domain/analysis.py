from typing import Union

from domain.value.date import Date


ProcessingTime = Union[float, None]
CountFiles = Union[int, None]


class Analysis:
    def __init__(self, count_files: CountFiles) -> None:
        self.date = Date()
        self.processing_time: ProcessingTime = None
        self.count_files: CountFiles = count_files

    def get_date(self) -> Date:
        return self.date

    def get_processing_time(self) -> ProcessingTime:
        return self.processing_time

    def set_processing_time(self, processing_time: ProcessingTime) -> None:
        self.processing_time = processing_time

    def get_count_files(self) -> CountFiles:
        return self.count_files

    def set_file_count(self, count_files: CountFiles) -> None:
        self.count_files = count_files
