from inputreader import aocinput
from typing import List, Tuple
import numpy as np


def neighborSlices(index: Tuple[int], shape: Tuple[int]) -> Tuple[slice]:  # includes index for the given point
    return tuple(slice(i-1 if i-1 >= 0 else 0, i+2 if i+2 < limit else limit) for i, limit in zip(index, shape))


def activeCubes(data: List[str], dimensions=3) -> int:
    cubes = np.zeros([len(data[0].strip()), len(data)] + [1] * (dimensions - 2))
    for x, line in enumerate(data):
        for y, char in enumerate(line.strip()):
            cubes[tuple([x, y] + [0] * (dimensions - 2))] = char == '#'

    for _ in range(6):
        cubes = np.pad(cubes, 1)  # add one extra layer each round due to expansion
        newcubes = np.zeros(cubes.shape)
        for index in np.ndindex(cubes.shape):
            activeNeighbors = np.sum(cubes[neighborSlices(index, cubes.shape)]) - cubes[index]
            if cubes[index] == 1 and 3 >= activeNeighbors >= 2:
                newcubes[index] = 1
            elif cubes[index] == 0 and activeNeighbors == 3:
                newcubes[index] = 1
        cubes = newcubes
    return np.sum(cubes)


def main(day):
    data = aocinput(day)
    result = activeCubes(data)
    result2 = activeCubes(data, 4)
    print(result, result2)


if __name__ == '__main__':
    main(17)
