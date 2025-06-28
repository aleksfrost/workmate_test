from data_order_by import DataOrderBy
from exceptions import OperatorError, FunctionError
import pytest


def test_order_float_asc_ok(full_data):
    data = full_data
    condition = "price=asc"
    res = DataOrderBy(data, condition).data_fuction()
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


def test_order_float_desc_ok(full_data):
    data = full_data
    condition = "price=desc"
    res = DataOrderBy(data, condition).data_fuction()
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

def test_order_str_asc_ok(not_full_data):
    data = not_full_data
    condition = "name=asc"
    res = DataOrderBy(data, condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
        ["iphone 15 pro","apple","999","4.9"],
        ["redmi note 12","xiaomi","199","4.6"],
    ]
    assert res == estimate_result


def test_order_str_desc_ok(not_full_data):
    data = not_full_data
    condition = "brand=desc"
    res = DataOrderBy(data[:4], condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
        ["redmi note 12","xiaomi","199","4.6"],
        ["galaxy s23 ultra","samsung","1199","4.8"],
        ["iphone 15 pro","apple","999","4.9"],
    ]
    assert res == estimate_result

def test_order_wrong_func(not_full_data):
    with pytest.raises(FunctionError):
        data = not_full_data
        condition = "price=dess"
        res = DataOrderBy(data, condition).data_fuction()
        return res

def test_order_wrong_operator(not_full_data):
    with pytest.raises(OperatorError):
        data = not_full_data
        condition = "price+desc"
        res = DataOrderBy(data, condition).data_fuction()
        return res

def test_order_no_data(header_only):
    data = header_only
    condition = "price=asc"
    res = DataOrderBy([data[0]], condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
    ]
    assert res == estimate_result

def test_order_empty_data(header_and_one):
    data = header_and_one
    condition = "price=asc"
    res = DataOrderBy(data, condition).data_fuction()
    estimate_result = [
        ["name","brand","price","rating"],
        ["iphone 15 pro","apple","999","4.9"],
    ]
    assert res == estimate_result