import argparse
import os
from datetime import datetime


def create_file(directories: str, file_name: str) -> None:
    os.makedirs(directories, exist_ok=True)
    full_path = os.path.join(directories, file_name)
    mode = "w" if not os.path.exists(full_path) else "a"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_number = 1
    with open(full_path, mode) as file:
        if mode == "a":
            file.write("\n\n")
        file.write(f"{timestamp}\n")
        while True:
            line = input("Enter content line: ")
            if line.lower().strip() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str, nargs="*")
    parser.add_argument("-f", "--filename", type=str)
    args = parser.parse_args()

    dirs = args.directory
    file_name = args.filename

    if dirs and file_name:
        directories = os.path.join(os.getcwd(), *dirs)
        file_name = file_name
    if not dirs and file_name:
        directories = os.getcwd()
        file_name = file_name
    if not file_name and dirs:
        directories = os.path.join(os.getcwd(), *dirs)
        file_name = "text.txt"

    create_file(directories, file_name)


if __name__ == "__main__":
    main()
