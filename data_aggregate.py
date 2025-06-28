from data_function import DataFunction


class DataAggregate(DataFunction):
    def __init__(self, data, condition):
        super().__init__(data, condition)
        self.operators = ["="]
        self.functions = ["avg", "min", "max"]

    def data_fuction(self):
        headers = self.data[0]
        work_data = self.data[1:]
        column, operator, cond = self.get_condition()
        enum_headers = enumerate(headers)
        for pair in enum_headers:
            if column in pair:
                number_column = pair[0]
        try:
            temp = float(work_data[0][number_column])
        except ValueError:
            raise ValueError(
                f"wrong column to aggregate, the data must be real or int number: {work_data[0][number_column]}")
        to_aggr = [float(data_row[number_column]) for data_row in work_data]
        if cond == "avg":
            result = sum(to_aggr) / len(to_aggr)
        elif cond == "min":
            result = min(to_aggr)
        elif cond == "max":
            result = max(to_aggr)
        return cond, result