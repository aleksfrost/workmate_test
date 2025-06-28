from abc import ABC, abstractmethod
import re

from exceptions import ExpressionError, FunctionError, OperatorError

class DataFunction(ABC):
    def __init__(self, data, condition) -> None:
        self.data: list = data
        self.condition: str = condition
        self.functions: list = None
        self.operators: list = None

    def is_data_to_proseed(self) -> bool:
        if len(self.data) <= 2:
            return False
        else:
            return True

    def get_condition(self):
        headers = self.data[0]
        part_condition = re.findall(r'[A-Za-z0-9.]+', self.condition)
        if len(part_condition) != 2:
            raise ExpressionError("Line in expression is wrong")
        if part_condition[0] in headers:
            if self.functions:
                if part_condition[1] in self.functions:
                    operator_check = self.condition.replace(part_condition[0], "").replace(part_condition[1], "")
                    if operator_check not in self.operators:
                        raise OperatorError(f"Entered operator not supported. Operator = {operator_check}, supported operators {self.operators}")
                else:
                    raise FunctionError(f"Function not supported or misspelled. Func = {part_condition[1]}, supported functions {self.functions}")
            else:
                operator_check = self.condition.replace(part_condition[0], "").replace(part_condition[1], "")
                if operator_check not in self.operators:
                    raise OperatorError(f"Entered operator not supported. Operator = {operator_check}, supported operators {self.operators}")
        else:
            raise ValueError(f"Entered wrong column name if any. Name = {part_condition}, columns names are {headers}")
        return part_condition[0], operator_check, part_condition[1]

    @abstractmethod
    def data_fuction(self) -> None:
        pass