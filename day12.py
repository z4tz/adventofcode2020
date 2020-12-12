from inputreader import aocinput
from typing import List, Tuple

directions = {'N': 0 + 1j,
              'S': 0 - 1j,
              'E': 1 + 0j,
              'W': -1 + 0j}

turn = {'L': 1j,
        'R': -1j}


def getDistance(instructions: List[Tuple[str, int]]) -> int:
    direction = directions['E']
    position = 0+0j  # starting position
    for move, distance in instructions:
        if move in directions:
            position += directions[move] * distance
        elif move in turn:
            direction *= turn[move] ** (distance//90)
        else:  # forward
            position += direction * distance

    return int(abs(position.real) + abs(position.imag))


def waypointMovement(instructions: List[Tuple[str, int]]) -> int:
    position = 0+0j
    waypoint = 10+1j  # waypoint is always relative to the ship
    for move, distance in instructions:
        if move in directions:
            waypoint += directions[move] * distance
        elif move in turn:
            waypoint *= turn[move] ** (distance//90)
        else:  # forward
            position += waypoint * distance

    return int(abs(position.real) + abs(position.imag))

def main(day):
    data = aocinput(day)
    instructions = [(line[0], int(line[1:])) for line in data]
    result = getDistance(instructions)
    result2 = waypointMovement(instructions)
    print(result, result2)


if __name__ == '__main__':
    main(12)
