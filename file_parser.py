import csv


def parse_csv(file_name: str) -> list | None:
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
    return data