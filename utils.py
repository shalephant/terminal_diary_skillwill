import json
from diarybook import Diary
def read_from_json_into_app(path):
    file = open(path)
    data = json.load(file.read())

    diaries = []

    for entry in data:
        diaries.append(Diary(entry["memo"], entry["tags"]))

    return diaries


