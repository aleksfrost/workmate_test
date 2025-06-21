import pytest
from main import parseCsv, aggregateCsv



def test_aggregation_avg():
    data = parseCsv('products.csv')
    condition = "price=avg"
    res = aggregateCsv(data, condition)
    assert res == ("avg", 602.0)


def test_aggregation_min():
    data = parseCsv('products.csv')
    condition = "price=min"
    res = aggregateCsv(data, condition)
    assert res == ("min", 149)


def test_aggregation_max():
    data = parseCsv('products.csv')
    condition = "rating=max"
    res = aggregateCsv(data, condition)
    assert res == ("max", 4.9)


def test_aggregation_wrong_func():
    with pytest.raises(ValueError):
        data = parseCsv('products.csv')
        condition = "rating=count"
        res = aggregateCsv(data, condition)


def test_aggregation_wrong_column():
    with pytest.raises(ValueError):
        data = parseCsv('products.csv')
        condition = "brand=avg"
        res = aggregateCsv(data, condition)
