class OperatorError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("caling str")
        if self.message:
            return f"OperatorError, {self.message}"
        else:
            return "OperatorError has been rised"


class FunctionError(OperatorError):

    def __str__(self):
        print("caling str")
        if self.message:
            return f"FunctionError, {self.message}"
        else:
            return "FunctionError has been rised"