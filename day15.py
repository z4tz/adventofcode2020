from inputreader import aocinput
from collections import defaultdict


def getNumber(data, target):
    numbers = defaultdict(int)
    for i, number in enumerate(data[0].split(',')[:-1]):
        numbers[int(number)] = i+1
    last = int(data[0].split(',')[-1])
    for i in range(len(numbers)+1, target):
        number = numbers[last]
        if number:
            number = i - number
        numbers[last] = i
        last = number
    return last


def main(day):
    data = aocinput(day)
    result = getNumber(data, 2020)
    result2 = getNumber(data, 30000000)
    print(result, result2)


if __name__ == '__main__':
    main(15)
