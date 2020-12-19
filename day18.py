from inputreader import aocinput
from typing import List, Callable
import re
from functools import reduce


def samePrecidence(expression: str) -> str:
    parts = expression.split(' ')
    total = int(parts[0])
    for i in range(1, len(parts), 2):
        total = eval(f'total {parts[i]} {parts[i+1]}')
    return str(total)


def plusPrecidence(expression: str) -> str:
    return str(reduce(lambda x, y: x*y, (eval(x) for x in expression.split("*"))))


def evalHomeWork(data: List[str], precidenceFunction: Callable) -> int:
    regex = re.compile(r'(\([\d /*+]*\))')
    totalSum = 0
    for line in data:
        while True:
            matches = regex.findall(line)
            if matches:
                for match in matches:
                    line = line.replace(match, precidenceFunction(match[1:-1]))  # dont pass any parenthesis
            else:
                totalSum += int(precidenceFunction(line))
                break
    return totalSum


def main(day):
    data = aocinput(day)
    result = evalHomeWork(data, samePrecidence)
    result2 = evalHomeWork(data, plusPrecidence)
    print(result, result2)


if __name__ == '__main__':
    main(18)
