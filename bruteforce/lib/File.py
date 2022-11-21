import os
from pathlib import Path

class File:
    def __init__(self, path):
        if not os.path.exists(path) and not Path(path).is_file():
            raise Exception(f"file at { path } is not exist !")
        self.path = path
    def read(self):
        with open(self.path, 'r') as file:
                self.content = file.read()
                # file.close()
                return self.content
    def write(self, content):
        with open(self.path, 'w') as file:
                file.write(content)
                # file.close()
    def delete(self):
        try:
            os.unlink(self.path)
        except Exception as e:
            raise Exception(e)