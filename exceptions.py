class CustomError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"OperatorError, {self.message}"
        else:
            return "OperatorError has been rised"


class FunctionError(CustomError):

    def __str__(self):
        if self.message:
            return f"FunctionError, {self.message}"
        else:
            return "FunctionError has been rised"

class ExpressionError(CustomError):

    def __str__(self):
        if self.message:
            return f"ExpressionError, {self.message}"
        else:
            return "ExpressionError has been rised"


class OperatorError(CustomError):

    def __str__(self):
        if self.message:
            return f"OperatorError, {self.message}"
        else:
            return "OperatorError has been rised"