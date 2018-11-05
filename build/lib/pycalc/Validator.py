from pycalc.Functions import *


def validate(string: str) -> str:
    string = string.replace(" ", "")
    string = combine_operator(string)

    string = string.replace('e', str(constants["e"]))
    string = string.replace('pi', str(constants["pi"]))

    i = 0
    while i < len(string) - 1:
        if (string[i].isnumeric() or string[i] == '.') and string[i + 1] == '(':
            string = string[0:i + 1] + '*' + string[i + 1:]
        elif string[i] == ')' and (string[i + 1].isnumeric() or string[i + 1] == '.'):
            string = string[0:i + 1] + '*' + string[i + 1:]
        elif string[i] == '^':
            expression = ''
            index = i

            while index < len(string) - 1:
                if string[index + 1].isnumeric():
                    expression = expression + string[index + 1]
                elif string[index + 1] == '^':
                    expression = expression + string[index + 1]
                else:
                    break

                index += 1

            if '^' in expression:
                string = string[:i + 1] + '(' + expression + ')' + string[index + 1:]

        i += 1

    return string


def add_brackets(string: str) -> str:
    start_index = 0
    while start_index <= len(string) - 1:
        if string[start_index] in ["-", "+"] and string[start_index + 1].isdigit() and \
                not string[start_index - 1].isdigit() and not string[start_index - 1] == ')':
            number = string[start_index] + string[start_index + 1]
            end_index = start_index + 1

            for index in range(start_index + 2, len(string)):
                try:
                    float(number + string[index])
                except ValueError:
                    break

                number = number + string[index]
                end_index += 1

            string = string[:start_index] + "(" + number + ")" + string[end_index + 1:]

            start_index = end_index
        start_index += 1

    return string


def combine_operator(string: str) -> str:
    for i in range(0, len(string) - 1):
        if i >= len(string):
            return string

        if string[i] in ["-", "+"] and string[i + 1] in ["-", "+"]:
            current = string[i]
            if current == "-" and string[i + 1] == "-":
                current = "+"
            elif current == "-" or string[i + 1] == "-":
                current = "-"
            else:
                return string

            string = string[:i] + current + string[i + 2:]
            string = combine_operator(string)

    return string


def split(string):
    def _process_operand(index):
        supposed_operand = string[index]
        index += 1
        while index < len(string) and not (string[index].isspace() or is_operator(string[index])):
            supposed_operand += string[index]
            index += 1
        try:
            if supposed_operand in arg_func:
                brackets_counter = 1
                index += 1
                begin = index
                while index < len(string) and brackets_counter != 0:
                    if Bracket.OPENED_BRACKET.value == string[index]:
                        brackets_counter += 1
                    elif Bracket.CLOSED_BRACKET.value == string[index]:
                        brackets_counter -= 1
                    index += 1
                expression.append([supposed_operand, split(string[begin:index - 1])])
            elif supposed_operand in constants:
                expression.append(float(constants[supposed_operand]))
            else:
                expression.append(float(supposed_operand))
        except ValueError:
            raise Exception("ERROR: '{}' is not operand".format(supposed_operand))
        return index

    def _process_operator(index):
        supposed_operator = string[index]
        if is_operator(supposed_operator):
            expression.append(supposed_operator)
        else:
            raise Exception("ERROR: '{}' is not operator".format(supposed_operator))
        return index + 1

    flag = True
    expression = []
    i = 0

    while True:
        while i < len(string) and string[i].isspace():
            i += 1

        if i >= len(string):
            break

        if Bracket.OPENED_BRACKET.value == string[i]:
            flag = False
        elif Bracket.CLOSED_BRACKET.value == string[i]:
            flag = False
            i = _process_operator(i)
            continue

        i = flag and _process_operand(i) or _process_operator(i)
        flag = not flag

    return expression
