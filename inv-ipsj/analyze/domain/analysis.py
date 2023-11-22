from typing import Union
from datetime import datetime


class Analysis:
    Id = str
    Name = str
    Date = str
    ProcessingTime = Union[float, None]
    CountFiles = Union[int, None]

    def __init__(self, name: Name, count_files: CountFiles = None) -> None:
        self.id: Analysis.Id = name  # torvalds/linux # 本当はnatural keyじゃなくてsurrogate keyにしたい
        self.name: Analysis.Name = name  # torvalds/linux
        self.date: Analysis.Date = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        self.processing_time: Analysis.ProcessingTime = None
        self.count_files: Analysis.CountFiles = count_files

    def get_id(self) -> Id:
        return self.id

    def get_name(self) -> Name:
        return self.name

    def get_date(self) -> Date:
        return self.date

    def get_processing_time(self) -> ProcessingTime:
        return self.processing_time

    def set_processing_time(self, processing_time: float) -> None:
        self.processing_time = processing_time

    def get_count_files(self) -> CountFiles:
        return self.count_files

    def set_file_count(self, count_files: int) -> None:
        self.count_files = count_files
