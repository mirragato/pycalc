from pycalc.Functions import *
from pycalc import Validator, Formatter


def calculate(expression):
    assert len(expression) > 0, "ERROR: Expression is missing."

    expression = Validator.validate(expression)
    expression = Validator.split(expression)

    formatted_expression = Formatter.formatter(expression)

    return calc(formatted_expression)


def calc(expression):
    length = len(expression)
    i = 0

    while i < length:
        token = expression[i]

        if token in operations:
            right = i - 2
            left = i - 1
            try:
                res = operations[token](expression[right], expression[left])
            except ArithmeticError:
                res = 0
            expression.insert(i + 1, res)
            expression = expression[:right] + expression[i + 1:]
            length = len(expression)
            j = expression.index(res)

            i = j + 1

            if j > length:
                break

            continue
        i += 1

    result = expression[0]

    return result
