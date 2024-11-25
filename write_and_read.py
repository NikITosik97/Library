import json


def read_file() -> dict:
    """Функция открывает файл на чтение и выдает сформированные данные в виде словаря"""

    with open("library.json", 'r', encoding='UTF-8') as f:
        data = json.load(f)

    return data


def write_file(data):
    """Функция открывает файл на запись, записывает полученные данные"""

    with open("library.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
