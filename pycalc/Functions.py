import math
from enum import Enum


def is_operator(operator):
    return [k for k, v in priorities.items() if v.__contains__(operator)]


class Bracket(Enum):
    OPENED_BRACKET = '('
    CLOSED_BRACKET = ')'


class Constants(Enum):
    E = "e"
    PI = "pi"


class ComparisonOperations(Enum):
    LESS = "<"
    MORE = ">"
    EQUAL = "="
    INEQUAL = "!="
    LESS_EQUAL = "<="
    MORE_EQUAL = ">="


class ArithmeticOperations(Enum):
    DIV = "/"
    DDIV = "//"
    POW = "^"
    PLUS = "+"
    MINUS = "-"
    MUL = "*"
    MOD = "%"


class OneArgOperations(Enum):
    ABS = "abs"
    FLOOR = "floor"
    ROUND = "round"
    SIN = "sin"
    COS = "cos"
    TAN = "tan"
    ASIN = "asin"
    ACOS = "acos"
    ATAN = "atan"
    SQRT = "sqrt"
    LOG = "log"
    LOG10 = "log10"


class TwoArgOperations(Enum):
    POW = "pow"


priorities = {
    5: [Bracket.OPENED_BRACKET.value, Bracket.CLOSED_BRACKET.value],
    4: [OneArgOperations.ATAN.value, OneArgOperations.ACOS.value, OneArgOperations.ASIN.value,
        OneArgOperations.TAN.value, OneArgOperations.COS.value, OneArgOperations.SIN.value,
        OneArgOperations.ABS.value, Constants.E.value],
    3: [TwoArgOperations.POW.value, ArithmeticOperations.POW.value, OneArgOperations.LOG10.value,
        OneArgOperations.LOG.value, OneArgOperations.SQRT.value],
    2: [ArithmeticOperations.MUL.value, ArithmeticOperations.DIV.value,
        ArithmeticOperations.MOD.value, ArithmeticOperations.DDIV.value],
    1: [ArithmeticOperations.PLUS.value, ArithmeticOperations.MINUS.value],
    0: [e.value for e in ComparisonOperations]
}

operations = {
    ComparisonOperations.LESS.value: lambda x, y: x < y,
    ComparisonOperations.MORE.value: lambda x, y: x > y,
    ComparisonOperations.EQUAL.value: lambda x, y: x == y,
    ComparisonOperations.INEQUAL.value: lambda x, y: x != y,
    ComparisonOperations.LESS_EQUAL.value: lambda x, y: x <= y,
    ComparisonOperations.MORE_EQUAL.value: lambda x, y: x >= y,

    ArithmeticOperations.PLUS.value: lambda x, y: x + y,
    ArithmeticOperations.MINUS.value: lambda x, y: x - y,
    ArithmeticOperations.POW.value: lambda x, y: x ** y,
    ArithmeticOperations.MUL.value: lambda x, y: x * y,
    ArithmeticOperations.DIV.value: lambda x, y: x / y,
    ArithmeticOperations.MOD.value: lambda x, y: x % y,
    ArithmeticOperations.DDIV.value: lambda x, y: x // y,
}

arg_func = {
    OneArgOperations.ABS.value: lambda x: abs(x),
    OneArgOperations.SIN.value: lambda x: math.sin(x),
    OneArgOperations.COS.value: lambda x: math.cos(x),
    OneArgOperations.TAN.value: lambda x: math.tan(x),
    OneArgOperations.ROUND.value: lambda x: round(x),
    OneArgOperations.FLOOR.value: lambda x: math.floor(x),
    OneArgOperations.ASIN.value: lambda x: math.asin(x),
    OneArgOperations.ACOS.value: lambda x: math.acos(x),
    OneArgOperations.ATAN.value: lambda x: math.atan(x),
    OneArgOperations.SQRT.value: lambda x: math.sqrt(x),
    OneArgOperations.LOG.value: lambda x: math.log(x),
    OneArgOperations.LOG10.value: lambda x: math.log10(x),
    TwoArgOperations.POW.value: lambda x, y: pow(x, y)
}

constants = {
    Constants.E.value: math.e,
    Constants.PI.value: math.pi
}
