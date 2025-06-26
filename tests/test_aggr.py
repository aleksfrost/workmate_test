import pytest
from exceptions import FunctionError, OperatorError
from main import parse_csv, aggregate_csv



def test_aggregation_avg():
    data = parse_csv('products.csv')
    condition = "price=avg"
    res = aggregate_csv(data, condition)
    assert res == ("avg", 602.0)


def test_aggregation_min():
    data = parse_csv('products.csv')
    condition = "price=min"
    res = aggregate_csv(data, condition)
    assert res == ("min", 149)


def test_aggregation_max():
    data = parse_csv('products.csv')
    condition = "rating=max"
    res = aggregate_csv(data, condition)
    assert res == ("max", 4.9)


def test_aggregation_wrong_func():
    with pytest.raises(OperatorError):
        data = parse_csv('products.csv')
        condition = "rating=count"
        res = aggregate_csv(data, condition)


def test_aggregation_wrong_column():
    with pytest.raises(ValueError):
        data = parse_csv('products.csv')
        condition = "brand=avg"
        res = aggregate_csv(data, condition)
