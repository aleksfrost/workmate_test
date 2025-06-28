import pytest
from exceptions import FunctionError, OperatorError
from data_aggregate import DataAggregate


@pytest.mark.parametrize(
        "cond, result",
        [
            ("price=avg", ("avg", 602.0)),
            ("price=min", ("min", 149)),
            ("rating=max", ("max", 4.9))
        ]

)
def test_aggregation(full_data, cond, result):
    res = DataAggregate(full_data, cond).data_fuction()
    assert res == result


def test_aggregation_wrong_func(not_full_data):
    with pytest.raises(FunctionError):
        data = not_full_data
        condition = "rating=count"
        res = DataAggregate(data, condition).data_fuction()
        return res


def test_aggregation_wrong_column(not_full_data):
    with pytest.raises(ValueError):
        data = not_full_data
        condition = "brand=avg"
        res = DataAggregate(data, condition).data_fuction()
        return res
