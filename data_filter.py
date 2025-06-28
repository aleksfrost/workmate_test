from data_function import DataFunction


class DataFilter(DataFunction):
    def __init__(self, data, condition):
        super().__init__(data, condition)
        self.operators = [">", "<", "="]

    def data_fuction(self):
        if self.is_data_to_proseed():
            headers = self.data[0]
            work_data = self.data[1:]
            column, operator, cond = self.get_condition()
            if operator == "=":
                operator = "=="
            enum_headers = enumerate(headers)
            for pair in enum_headers:
                if column in pair:
                    number_column = pair[0]
            try:
                temp = float(cond)
                result = [data_row for data_row in work_data if eval(
                    f"{data_row[number_column]} {operator} {temp}")]
            except:
                result = [data_row for data_row in work_data if eval(
                    f"'{data_row[number_column]}' {operator} '{cond}'")]
            if result:
                result.insert(0, headers)
            return result
        else:
            return self.data
