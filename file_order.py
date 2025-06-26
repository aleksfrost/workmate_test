from exceptions import FunctionError, OperatorError


def order_csv(data: list, condition: str) -> list | None:
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
                    result = sorted(
                        data[1:], key=lambda x: float(x[number_column]))
                except Exception:
                    result = sorted(data[1:], key=lambda x: x[number_column])
            elif col_data == "desc":
                try:
                    float(data[1][number_column])
                    result = sorted(data[1:], key=lambda x: float(
                        x[number_column]), reverse=True)
                except Exception:
                    result = sorted(
                        data[1:], key=lambda x: x[number_column], reverse=True)
            else:
                raise FunctionError(
                    f"Function for parameter '--order-by' not supported or wrong")
            result.insert(0, headers)
        else:
            raise OperatorError(
                f"Operator for parameter '--order-by' not supported or wrong")
    return result