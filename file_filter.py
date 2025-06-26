from exceptions import FunctionError


def filter_csv(data: list, condition: str) -> list | None:
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
                raise ValueError(
                    f"--where condition is wrong. there is no column: {col}")
            try:
                float(col_data)
                result = [data_row for data_row in data[1:] if eval(
                    f"{data_row[number_column]} {operator} {float(col_data)}")]
            except:
                result = [data_row for data_row in data[1:] if eval(
                    f"'{data_row[number_column]}' {operator} '{col_data}'")]
            if result:
                result.insert(0, headers)
            return result
    raise FunctionError(f"Unsupported parameter in '--where' condition")