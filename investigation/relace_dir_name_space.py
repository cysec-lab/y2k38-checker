import os
import glob


def replace_dir_name_space(dir: str):
    def find_all_files(directory):
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                print(file)
                yield os.path.join(root, file)

            for d in dirs:
                yield os.path.join(root, d)
    
    for path in find_all_files(dir):
        if " " in path:
            print(path)
            os.rename(path, path.replace(" ", "__"))



if __name__ == "__main__":
    replace_dir_name_space("./c")