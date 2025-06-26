from main import parse_csv, filter_csv, aggregate_csv


def test_filter_aggr_ok():
    data = parse_csv('products.csv')
    condition = "brand=apple"
    res_f = filter_csv(data, condition)
    condition = "price=min"
    res = aggregate_csv(res_f, condition)
    estimate_result = ("min", 429)
    assert res == estimate_result