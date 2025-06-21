import argparse
from tabulate import tabulate
import csv

def createParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--where")
    parser.add_argument("--aggregate")
    parser.add_argument("--order-by")

    return parser


def parseCsv(file_name: str) -> list|None:
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
    return data


def filterCsv(data: list, condition: str) -> list|None:
    col = None
    col_data = None
    headers = data[0]
    enum_headers = enumerate(headers)
    operators = ['>', '<', '=']
    result = []
    for operator in operators:
        if operator in condition:
            number_column = None
            col, col_data = condition.split(operator)
            if operator == "=":
                operator = "=="
            for pair in enum_headers:
                if col in pair:
                    number_column = pair[0]
            if not number_column:
                raise ValueError(f"--where condition is wrong. there is no column: {col}")
            try:
                float(col_data)
                result = [data_row for data_row in data[1:] if eval(f"{data_row[number_column]} {operator} {float(col_data)}")]
            except:
                result = [data_row for data_row in data[1:] if eval(f"'{data_row[number_column]}' {operator} '{col_data}'")]
            if result:
                result.insert(0, headers)
            return result
    raise ValueError(f"Unsupported parameter in '--where' condition")



def aggregateCsv(data: list, condition: str) -> tuple:
    col = None
    col_data = None
    headers = data[0]
    enum_headers = enumerate(headers)
    if "=" in condition:
        number_column = None
        col, col_data = condition.split("=")
        for pair in enum_headers:
            if col in pair:
                number_column = pair[0]
        try:
            float(data[1][number_column])
        except ValueError:
            raise ValueError(f"wrong column to aggregate, the data must be real or int number: {data[1][number_column]}")
        to_aggr = [float(data_row[number_column]) for data_row in data[1:]]
        if col_data == "avg":
            result = sum(to_aggr) / len(to_aggr)
        elif col_data == "min":
            result = min(to_aggr)
        elif col_data == "max":
            result = max(to_aggr)
        else:
            raise ValueError(f"Operator for parameter '--aggregate' not supported or wrong")
    return col_data, result



def orderCsv(data: list, condition: str) -> list|None:
    if len(data) == 1 or len(data) == 2:
        result = data
    else:
        col = None
        col_data = None
        headers = data[0]
        enum_headers = enumerate(headers)

        if "=" in condition:
            number_column = None
            col, col_data = condition.split("=")
            for pair in enum_headers:
                if col in pair:
                    number_column = pair[0]
            if col_data == "asc":
                try:
                    float(data[1][number_column])
                    result = sorted(data[1:], key=lambda x: float(x[number_column]))
                except Exception:
                    result = sorted(data[1:], key=lambda x: x[number_column])
            elif col_data == "desc":
                try:
                    float(data[1][number_column])
                    result = sorted(data[1:], key=lambda x: float(x[number_column]), reverse=True)
                except Exception:
                    result = sorted(data[1:], key=lambda x: x[number_column], reverse=True)
            else:
                raise ValueError(f"Function for parameter '--order-by' not supported or wrong")
            result.insert(0, headers)
        else:
            raise ValueError(f"Operator for parameter '--order-by' not supported or wrong")
    return result

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    if namespace.file:
        data = parseCsv(namespace.file)
    else:
        raise ValueError(f"There must be file name")
    if namespace.where:
        if len(data) > 1:
            data = filterCsv(data, namespace.where)
        else:
            raise ValueError("There is no data")
    if namespace.aggregate:
        if len(data) > 1:
            aggr_func, aggr_result = aggregateCsv(data, namespace.aggregate)
            data = [[aggr_func], [aggr_result]]
    if namespace.order_by:
        if len(data) > 1:
            data = orderCsv(data, namespace.order_by)
    table = tabulate(data[1:], data[0], tablefmt="grid")
    print(table)
