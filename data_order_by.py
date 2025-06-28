from data_function import DataFunction

class DataOrderBy(DataFunction):
    def __init__(self, data, condition):
        super().__init__(data, condition)
        self.operators = ["="]
        self.functions = ["asc", "desc"]

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
            if cond == "asc":
                try:
                    float(work_data[0][number_column])
                    result = sorted(
                        work_data, key=lambda x: float(x[number_column]))
                except Exception:
                    result = sorted(work_data, key=lambda x: x[number_column])
            elif cond == "desc":
                try:
                    float(work_data[0][number_column])
                    result = sorted(work_data, key=lambda x: float(
                        x[number_column]), reverse=True)
                except Exception:
                    result = sorted(
                        work_data, key=lambda x: x[number_column], reverse=True)
            result.insert(0, headers)
            return result
        else:
            return self.data