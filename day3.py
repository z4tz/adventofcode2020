from inputreader import aocinput
from typing import List
from functools import reduce


def treeEncounters(trees: List[List[bool]], sidesteps: int = 3, straightsteps: int = 1) -> int:
    width = len(trees[0])
    column = 0
    count = 0
    for row in range(0, len(trees), straightsteps):
        if trees[row][column]:
            count += 1
        column = (column + sidesteps) % width
    return count


def minimizeEncounters(trees: List[List[bool]]) -> int:
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    encounters = [treeEncounters(trees, *slope) for slope in slopes]
    return reduce(lambda x, y: x * y, encounters)


def main(day):
    data = aocinput(day)
    data = [[char == '#' for char in line.strip()] for line in data]
    result1 = treeEncounters(data)
    result2 = minimizeEncounters(data)
    print(result1, result2)


if __name__ == '__main__':
    main(3)
