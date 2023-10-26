import os
import json

json_file = open("save.json", "r")
json_obj = json.load(json_file)
for obj in json_obj:
    dataset_file = open("dataset.jsonl", "a")
    write_data = {
        "messages": [
            {"role": "system", "content": "あなたはしんぶんぶんという20歳の学生エンジニアです"},
            {"role": "user", "content": obj['q']},
            {"role": "assistant", "content": obj['a']},
        ]
    }
    dataset_file.write(json.dumps(write_data, ensure_ascii=False) + "\n")
