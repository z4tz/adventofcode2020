from inputreader import aocinput
from typing import List
import re


def validPasswords(data: List[str]):
    regex = re.compile('(?P<min>\d+)-(?P<max>\d+) (?P<letter>.): (?P<password>.+)')
    part1 = 0
    part2 = 0
    for line in data:
        result = regex.match(line)
        password = result.group('password')
        firstNumber = int(result.group('min'))
        secondNumber = int(result.group('max'))
        letter = result.group('letter')

        if secondNumber >= password.count(letter) >= firstNumber:
            part1 += 1

        if (password[firstNumber-1] + password[secondNumber-1]).count(letter) == 1:
            part2 += 1
    return part1, part2


def main(day):
    data = aocinput(day)
    result = validPasswords(data)
    print(result)


if __name__ == '__main__':
    main(2)
