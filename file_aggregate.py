from exceptions import OperatorError


def aggregate_csv(data: list, condition: str) -> tuple:
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
            raise ValueError(
                f"wrong column to aggregate, the data must be real or int number: {data[1][number_column]}")
        to_aggr = [float(data_row[number_column]) for data_row in data[1:]]
        if col_data == "avg":
            result = sum(to_aggr) / len(to_aggr)
        elif col_data == "min":
            result = min(to_aggr)
        elif col_data == "max":
            result = max(to_aggr)
        else:
            raise OperatorError(
                f"Operator for parameter '--aggregate' not supported or wrong")
    return col_data, result