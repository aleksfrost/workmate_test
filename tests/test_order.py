from main import parse_csv, order_csv
from exceptions import OperatorError, FunctionError
import pytest


def test_order_float_asc_ok():
    data = parse_csv('products.csv')
    condition = "price=asc"
    res = order_csv(data, condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["redmi 10c","xiaomi","149","4.1"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["poco x5 pro","xiaomi","299","4.4"],
        ["galaxy a54","samsung","349","4.2"],
        ["iphone se","apple","429","4.1"],
        ["iphone 13 mini","apple","599","4.5"],
        ["iphone 14","apple","799","4.7"],
        ["iphone 15 pro","apple","999","4.9"],
        ["galaxy z flip 5","samsung","999","4.6"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
    ]
    assert res == estimate_result


def test_order_float_desc_ok():
    data = parse_csv('products.csv')
    condition = "price=desc"
    res = order_csv(data, condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
        ["iphone 15 pro","apple","999","4.9"],
        ["galaxy z flip 5","samsung","999","4.6"],
        ["iphone 14","apple","799","4.7"],
        ["iphone 13 mini","apple","599","4.5"],
        ["iphone se","apple","429","4.1"],
        ["galaxy a54","samsung","349","4.2"],
        ["poco x5 pro","xiaomi","299","4.4"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["redmi 10c","xiaomi","149","4.1"],
    ]
    assert res == estimate_result

def test_order_str_asc_ok():
    data = parse_csv('products.csv')
    condition = "name=asc"
    res = order_csv(data[:4], condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
        ["iphone 15 pro","apple","999","4.9"],
        ["redmi note 12","xiaomi","199","4.6"],
    ]
    assert res == estimate_result


def test_order_str_desc_ok():
    data = parse_csv('products.csv')
    condition = "brand=desc"
    res = order_csv(data[:4], condition)
    estimate_result = [
        ["name","brand","price","rating"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
        ["iphone 15 pro","apple","999","4.9"],
    ]
    assert res == estimate_result

def test_order_wrong_func():
    with pytest.raises(FunctionError):
        data = parse_csv('products.csv')
        condition = "price=dess"
        res = order_csv(data, condition)

def test_order_wrong_operator():
    with pytest.raises(OperatorError):
        data = parse_csv('products.csv')
        condition = "price+desc"
        res = order_csv(data, condition)

def test_order_no_data():
    data = parse_csv('products.csv')
    condition = "price=asc"
    res = order_csv([data[0]], condition)
    estimate_result = [
        ["name","brand","price","rating"],
    ]
    assert res == estimate_result

def test_order_empty_data():
    condition = "price=asc"
    res = order_csv([[]], condition)
    estimate_result = [[]]
    assert res == estimate_result