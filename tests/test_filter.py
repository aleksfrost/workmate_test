from exceptions import OperatorError
from main import parse_csv, filter_csv, aggregate_csv
import pytest


def test_file_is_ok():
    res = parse_csv('products.csv')
    assert type(res) == list

def test_file_is_not_ok():
    with pytest.raises(FileNotFoundError):
        res = parse_csv('product.csv')

def test_filter_string():
    data = parse_csv('products.csv')
    condition = "brand=apple"
    res = filter_csv(data, condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["iphone 15 pro","apple","999","4.9"],
        ["iphone 14","apple","799","4.7"],
        ["iphone se","apple","429","4.1"],
        ["iphone 13 mini","apple","599","4.5"],
    ]
    assert res == estimate_result

def test_filter_float():
    data = parse_csv('products.csv')
    condition = "rating>4.5"
    res = filter_csv(data, condition)
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
    data = parse_csv('products.csv')
    condition = "price<500"
    res = filter_csv(data, condition)
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
    with pytest.raises(OperatorError):
        data = parse_csv('products.csv')
        condition = "price-500"
        res = filter_csv(data, condition)

def test_fiter_condition_wrong_column():
    with pytest.raises(ValueError):
        data = parse_csv('products.csv')
        condition = "mice=500"
        res = filter_csv(data, condition)


