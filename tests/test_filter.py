from main import parseCsv, filterCsv, aggregateCsv
import pytest



def test_file_is_ok():
    res = parseCsv('products.csv')
    assert type(res) == list

def test_file_is_not_ok():
    with pytest.raises(FileNotFoundError):
        res = parseCsv('product.csv')




def test_filter_string():
    data = parseCsv('products.csv')
    condition = "brand=apple"
    res = filterCsv(data, condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["iphone 15 pro","apple","999","4.9"],
        ["iphone 14","apple","799","4.7"],
        ["iphone se","apple","429","4.1"],
        ["iphone 13 mini","apple","599","4.5"],
    ]
    assert res == estimate_result


def test_filter_float():
    data = parseCsv('products.csv')
    condition = "rating>4.5"
    res = filterCsv(data, condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["iphone 15 pro","apple","999","4.9"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["iphone 14","apple","799","4.7"],
        ["galaxy z flip 5","samsung","999","4.6"],
    ]
    assert res == estimate_result


def test_filter_int():
    data = parseCsv('products.csv')
    condition = "price<500"
    res = filterCsv(data, condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["galaxy a54","samsung","349","4.2"],
        ["poco x5 pro","xiaomi","299","4.4"],
        ["iphone se","apple","429","4.1"],
        ["redmi 10c","xiaomi","149","4.1"],
    ]
    assert res == estimate_result


def test_fiter_condition_not_ok():
    with pytest.raises(ValueError):
        data = parseCsv('products.csv')
        condition = "price-500"
        res = filterCsv(data, condition)


def test_fiter_condition_wrong_column():
    with pytest.raises(ValueError):
        data = parseCsv('products.csv')
        condition = "mice=500"
        res = filterCsv(data, condition)


