import re


def arithmetic_arranger(problems, calc=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    line1 = ""
    line2 = ""
    lines = ""
    solution = ""
    for problem in problems:
        if re.search("[^\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        # splitting the looped problem
        n1 = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        n2 = problem.split(" ")[2]
        if len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."
        result = ""
        if operator == "+":
            result = str(int(n1) + int(n2))
        elif operator == "-":
            result = str(int(n1) - int(n2))
        space = max(len(n1), len(n2)) + 2
        first = str(n1).rjust(space)
        second = operator + str(n2).rjust(space - 1)
        line = ""
        value = str(result).rjust(space)
        for _ in range(space):
            line += "-"
        if problem != problems[-1]:
            line1 += first + "    "
            line2 += second + "    "
            lines += line + "    "
            solution += value + "    "
        else:
            line1 += first
            line2 += second
            lines += line
            solution += value
    if calc:
        string = line1 + "\n" + line2 + "\n" + lines + "\n" + solution
    else:
        string = line1 + "\n" + line2 + "\n" + lines
    return string
