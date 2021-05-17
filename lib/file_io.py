import json
import yaml

IN_PATH = "./io_file/input.json"
IN_PATH_2 = "./io_file/input2.json"
OUT_PATH = "./io_file/output.json"
DISPLAY_PATH = "./io_file/display"

class StrIO:
    @staticmethod
    def read(path=IN_PATH, mode="r"):
        with open(path, mode, encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def write(data, path=OUT_PATH, mode="w"):
        with open(path, mode, encoding="utf-8") as f:
            f.write(data)

class JsonIO:
    @staticmethod
    def load(path=IN_PATH, mode="r"):
        """ test.jsonからデータ読み込み """
        with open(path, mode, encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def dump(json_data, path=OUT_PATH, mode="w"):
        """ result.jsonに結果を出力 """
        with open(path, mode, encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        return

class YamlIO:
    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, mode="r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def dump(self, data):
        with open(self.path, mode="w", encoding="utf-8") as f:
            data = yaml.dump(
                data, f,
                indent=2,
                encoding='utf-8',
                allow_unicode=True
            )


class CsvIO:
    def load(self): pass
    def dump(self, data): pass
