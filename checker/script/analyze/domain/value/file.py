import os

Path = str


class File:
    def __init__(self, path) -> None:
        if os.path.exists(path):  # case for absolute path
            self.paths = path
        elif os.path.exists(os.path.join(os.getcwd(), path)):  # case for relative path
            self.paths = os.path.join(os.getcwd(), path)
        else:
            raise FileNotFoundError("Error: File not found: " + path)

    def get_path(self) -> Path:
        return self.paths
