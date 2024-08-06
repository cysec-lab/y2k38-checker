import os

Path = str


class File:
    def __init__(self, path) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError("Error: File not found: " + path)
        self.paths = os.path.abspath(path)

    def get_path(self) -> Path:
        return self.paths
