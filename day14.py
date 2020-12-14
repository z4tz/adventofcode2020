from inputreader import aocinput
from typing import List
from itertools import product


def memorySum(data: List[str]) -> int:
    memory = {}
    for line in data:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        else:
            parts = line.split('=')
            adress = int(parts[0].strip()[4:-1])
            value = bin(int(parts[1]))[2:]
            memory[adress] = applymask(value, mask)
    return sum(memory.values())


def applymask(value: str, mask: str) -> int:
    return int(''.join(m if m != 'X' else v for v, m in zip(value.zfill(36), mask)), 2)


def memorySum2(data: List[str]) -> int:
    memory = {}
    for line in data:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        else:
            parts = line.split('=')
            adress = bin(int(parts[0].strip()[4:-1]))[2:]
            value = int(parts[1])
            for decodedAdress in adressMask(adress, mask):
                memory[decodedAdress] = value
    return sum(memory.values())


def adressMask(adress: str, mask: str) -> List[int]:
    adress = [m if m != '0' else v for v, m in zip(adress.zfill(36), mask)]  # overwrite 1s and Xs from mask
    positions = [i for i, char in enumerate(adress) if char == 'X']
    adresses = []
    for permutation in product('01', repeat=len(positions)):  # put in all possible combinations of 0 and 1 where X
        for i, number in zip(positions, permutation):
            adress[i] = number
        adresses.append(int(''.join(adress), 2))
    return adresses


def main(day):
    data = aocinput(day)
    result = memorySum(data)
    result2 = memorySum2(data)
    print(result, result2)


if __name__ == '__main__':
    main(14)
