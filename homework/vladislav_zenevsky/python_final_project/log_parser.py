import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path', help='Full path to the log folder')
parser.add_argument('-t', '--text', help='Text to search in the log')
args = parser.parse_args()


def read_file():
    if os.path.exists(args.path):
        print(f"Path exists: {args.path}")
        for file_name in os.listdir(args.path):
            file_path = os.path.join(args.path, file_name)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r') as file:
                        line_number = 1
                        while True:
                            line = file.readline()
                            if not line:
                                break
                            yield file_path, line_number, line
                            line_number += 1
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    else:
        print(f"Path does not exist: {args.path}")


for data_file_path, data_line_number, data_log_line in read_file():
    if args.text in data_log_line:
        log_words = data_log_line.split()
        start = max(0, log_words.index(args.text.split()[0]) - 5)
        end = min(len(log_words), log_words.index(args.text.split()[-1]) + 6)
        log = ' '.join(log_words[start:end])
        print(f'file: {data_file_path}, line: {data_line_number}, log: {log}')
