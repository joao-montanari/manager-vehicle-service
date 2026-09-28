import json


def get_json_data(file: str):
    with open(f"mock/{file}.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    data_list = data["trips"]

    return data_list