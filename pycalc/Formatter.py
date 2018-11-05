from pycalc.Functions import *
from pycalc import Calc


def formatter(expression):
    operators = []
    tokens = []

    for token in expression:
        if type(token) is list:
            func = token[0]
            sub_expression = token[1]
            tokens.append(arg_func[func](Calc.calc(formatter(sub_expression))))
        elif is_operator(token):
            if Bracket.CLOSED_BRACKET.value == token:
                tmp = operators.pop()
                while Bracket.OPENED_BRACKET.value != tmp:
                    tokens.append(tmp)
                    tmp = operators.pop()
            elif Bracket.OPENED_BRACKET.value == token:
                operators.append(token)
            else:
                if len(operators):

                    if [k for k, v in priorities.items() if v.__contains__(token)] <= \
                            [k for k, v in priorities.items() if v.__contains__(operators[-1])]:
                        if Bracket.OPENED_BRACKET.value != operators[-1]:
                            tokens.append(operators.pop())
                operators.append(token)
        else:
            tokens.append(token)

    while len(operators) > 0:
        tokens.append(operators.pop())

    return tokens
