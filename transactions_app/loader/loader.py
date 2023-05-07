from json import load, JSONDecodeError


class JSONFileLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                return self.load_json_file(file)
        except FileNotFoundError:
            raise FileNotFoundError('Error: File not found.')

    def load_json_file(self, file):
        try:
            return load(file)
        except JSONDecodeError:
            raise ValueError('Error: Invalid JSON file.')
