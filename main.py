import argparse
from tabulate import tabulate
from file_parser import parse_csv
from file_filter import filter_csv
from file_aggregate import aggregate_csv
from file_order import order_csv


def createParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--where")
    parser.add_argument("--aggregate")
    parser.add_argument("--order-by")

    return parser


if __name__ == '__main__':

    parser = createParser()
    namespace = parser.parse_args()

    if namespace.file:
        data = parse_csv(namespace.file)
    else:
        raise ValueError(f"There must be file name")
    if namespace.where:
        if len(data) > 1:
            data = filter_csv(data, namespace.where)
        else:
            raise ValueError("There is no data")
    if namespace.aggregate:
        if len(data) > 1:
            aggr_func, aggr_result = aggregate_csv(data, namespace.aggregate)
            data = [[aggr_func], [aggr_result]]
    if namespace.order_by:
        if len(data) > 1:
            data = order_csv(data, namespace.order_by)
    table = tabulate(data[1:], data[0], tablefmt="grid")
    print(table)
