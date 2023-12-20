import json


def read(file):
    try:
        with open(f'{file}', 'r', encoding="utf-8") as f:
            data = json.load(f)
            try:
                return data
            except OSError:
                return 'Cannot read data!'
    except FileNotFoundError:
        return 'File not found!'
