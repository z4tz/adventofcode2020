from inputreader import aocinput
from typing import List, Tuple


def highestSeat(data: List[str]) -> Tuple[int, int]:
    seatIDs = []
    for line in data:
        row = int(''.join(['1' if char is 'B' else '0' for char in line[:7]]), 2)
        col = int(''.join(['1' if char is 'R' else '0' for char in line[7:10]]), 2)
        seatIDs.append(row * 8 + col)
    return max(seatIDs), sum(range(min(seatIDs), max(seatIDs) + 1)) - sum(seatIDs)


def main(day):
    data = aocinput(day)
    result = highestSeat(data)
    print(result)


if __name__ == '__main__':
    main(5)
