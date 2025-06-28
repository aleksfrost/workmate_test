from exceptions import OperatorError
from data_filter import DataFilter
import pytest


def test_filter_string(full_data):
    data = full_data
    condition = "brand=apple"
    res = DataFilter(data, condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
        ["iphone 15 pro","apple","999","4.9"],
        ["iphone 14","apple","799","4.7"],
        ["iphone se","apple","429","4.1"],
        ["iphone 13 mini","apple","599","4.5"],
    ]
    assert res == estimate_result

def test_filter_float(full_data):
    data = full_data
    condition = "rating>4.5"
    res = DataFilter(data, condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
        ["iphone 15 pro","apple","999","4.9"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["iphone 14","apple","799","4.7"],
        ["galaxy z flip 5","samsung","999","4.6"],
    ]
    assert res == estimate_result

def test_filter_int(full_data):
    data = full_data
    condition = "price<500"
    res = DataFilter(data, condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["galaxy a54","samsung","349","4.2"],
        ["poco x5 pro","xiaomi","299","4.4"],
        ["iphone se","apple","429","4.1"],
        ["redmi 10c","xiaomi","149","4.1"],
    ]
    assert res == estimate_result

def test_fiter_condition_not_ok(full_data):
    with pytest.raises(OperatorError):
        data = full_data
        condition = "price-500"
        res = DataFilter(data, condition).data_fuction()
        return res

def test_fiter_condition_wrong_column(full_data):
    with pytest.raises(ValueError):
        data = full_data
        condition = "mice=500"
        res = DataFilter(data, condition).data_fuction()
        return res

def test_filter_header(header_only):
    data = header_only
    condition = "brand=apple"
    res = DataFilter(data, condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
    ]
    assert res == estimate_result

def test_filter_header_and_one(header_and_one):
    data = header_and_one
    condition = "rating>4.5"
    res = DataFilter(data, condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
        ["iphone 15 pro","apple","999","4.9"],
    ]
    assert res == estimate_result


