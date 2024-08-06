import time


class Timer:
    def __init__(self) -> None:
        self.time: float = 0

    def start(self) -> None:
        self.start_time = time.perf_counter()

    def stop(self) -> None:
        self.time = time.perf_counter() - self.start_time

    def get_time(self) -> float:
        return self.time
