from typing import TypedDict
from datetime import datetime


class Analysis:
    Id = str
    Name = str
    Date = str
    ProcessingTime = float

    def __init__(self, name: Name) -> None:
        self.id: Analysis.Id = name  # torvalds/linux # 本当はnatural keyじゃなくてsurrogate keyにしたい
        self.name: Analysis.Name = name  # torvalds/linux
        self.date: Analysis.Date = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        self.processing_time: Analysis.ProcessingTime = None

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_date(self) -> str:
        return self.date

    def get_processing_time(self) -> float:
        return self.processing_time

    def set_processing_time(self, processing_time: float) -> None:
        self.processing_time = processing_time
