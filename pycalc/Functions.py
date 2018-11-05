import math
from enum import Enum


def is_operator(operator):
    return operator in priorities


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
    Bracket.OPENED_BRACKET.value: float("inf"),
    Bracket.CLOSED_BRACKET.value: float("inf"),

    Constants.E.value: 4,
    OneArgOperations.ABS.value: 4,
    OneArgOperations.SIN.value: 4,
    OneArgOperations.COS.value: 4,
    OneArgOperations.TAN.value: 4,
    OneArgOperations.ASIN.value: 4,
    OneArgOperations.ACOS.value: 4,
    OneArgOperations.ATAN.value: 4,

    OneArgOperations.SQRT.value: 3,
    OneArgOperations.LOG.value: 3,
    OneArgOperations.LOG10.value: 3,
    ArithmeticOperations.POW.value: 3,
    TwoArgOperations.POW.value: 3,

    ArithmeticOperations.MUL.value: 2,
    ArithmeticOperations.DIV.value: 2,
    ArithmeticOperations.MOD.value: 2,
    ArithmeticOperations.DDIV.value: 2,

    ArithmeticOperations.PLUS.value: 1,
    ArithmeticOperations.MINUS.value: 1,

    ComparisonOperations.LESS.value: 0,
    ComparisonOperations.MORE.value: 0,
    ComparisonOperations.EQUAL.value: 0,
    ComparisonOperations.INEQUAL.value: 0,
    ComparisonOperations.LESS_EQUAL.value: 0,
    ComparisonOperations.MORE_EQUAL.value: 0
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
