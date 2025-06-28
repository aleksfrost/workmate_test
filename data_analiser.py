from tabulate import tabulate
from exceptions import ExpressionError
from file_parser import parse_csv
from data_filter import DataFilter
from data_aggregate import DataAggregate
from data_order_by import DataOrderBy


class DataAnaliser():

    def __init__(self, namespace):
        self.namespace = namespace

    def script(self):
        if self.namespace.file:
            data = parse_csv(self.namespace.file)
        else:
            raise ExpressionError(f"There must be file name")
        if self.namespace.where:
            data = DataFilter(data, self.namespace.where).data_fuction()
        if self.namespace.aggregate:
            aggr_func, aggr_result = DataAggregate(data, self.namespace.aggregate).data_fuction()
            data = [[aggr_func], [aggr_result]]
        if self.namespace.order_by:
            data = DataOrderBy(data, self.namespace.order_by).data_fuction()
        table = tabulate(data[1:], data[0], tablefmt="grid")
        print(table)