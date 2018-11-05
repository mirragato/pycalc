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
    Bracket.OPENED_BRACKET: float("inf"),
    Bracket.CLOSED_BRACKET: float("inf"),

    Constants.E: 4,
    OneArgOperations.ABS: 4,
    OneArgOperations.SIN: 4,
    OneArgOperations.COS: 4,
    OneArgOperations.TAN: 4,
    OneArgOperations.ASIN: 4,
    OneArgOperations.ACOS: 4,
    OneArgOperations.ATAN: 4,

    OneArgOperations.SQRT: 3,
    OneArgOperations.LOG: 3,
    OneArgOperations.LOG10: 3,
    ArithmeticOperations.POW: 3,
    TwoArgOperations.POW: 3,

    ArithmeticOperations.MUL: 2,
    ArithmeticOperations.DIV: 2,
    ArithmeticOperations.MOD: 2,
    ArithmeticOperations.DDIV: 2,

    ArithmeticOperations.PLUS: 1,
    ArithmeticOperations.MINUS: 1,

    ComparisonOperations.LESS: 0,
    ComparisonOperations.MORE: 0,
    ComparisonOperations.EQUAL: 0,
    ComparisonOperations.INEQUAL: 0,
    ComparisonOperations.LESS_EQUAL: 0,
    ComparisonOperations.MORE_EQUAL: 0
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
