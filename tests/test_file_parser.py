from exceptions import OperatorError
from data_filter import DataFilter
from file_parser import parse_csv
import pytest

def test_file_name(full_data):
    file_name = "products.csv"
    res = parse_csv(file_name)
    assert full_data == res
