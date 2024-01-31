import json


def of(dict_list):
    return json.dumps(dict_list, ensure_ascii=False)


def save(filepath, json_data):
    with open(filepath, 'w', encoding="UTF-8") as file:
        file.write(json_data)

