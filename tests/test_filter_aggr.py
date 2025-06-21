from main import parseCsv, filterCsv, aggregateCsv
import pytest


def test_filter_aggr_ok():
    data = parseCsv('products.csv')
    condition = "brand=apple"
    res_f = filterCsv(data, condition)
    condition = "price=min"
    res = aggregateCsv(res_f, condition)
    estimate_result = ("min", 429)
    assert res == estimate_result