from datetime import datetime


class Date:
    def __init__(self) -> None:
        self.date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def get_date(self) -> str:
        return self.date
