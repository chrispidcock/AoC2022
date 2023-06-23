import os

absolute_path = os.path.dirname(__file__)
relative_path = "../input_files/"

def read_file(file_name: str) -> str:
    file_path = os.path.join(absolute_path, relative_path, file_name)
    lines = []
    with open(file_path, "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines
