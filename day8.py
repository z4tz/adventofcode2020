from inputreader import aocinput
from typing import List, Union, Tuple


def oneVisit(instructions: List[List[Union[str, int]]]) -> Tuple[int, int]:
    accumulator = 0
    position = 0

    visited = set()
    exitcode = 0
    terminationPosition = len(instructions)
    while True:
        visited.add(position)
        operation, argument = instructions[position]
        if 'acc' == operation:
            accumulator += argument
        elif 'jmp' == operation:
            position += argument - 1
        position += 1

        if position in visited:
            exitcode = 1
            break
        if position == terminationPosition:
            break

    return accumulator, exitcode


def findBrokenInstruction(instructions: List[List[Union[str, int]]]) -> int:
    exitcode = 1
    accumulator = 0
    i = len(instructions)-1
    while exitcode == 1:
        operation, argument = instructions[i]
        if operation != 'acc':
            tempinstructions = instructions.copy()
            if operation == 'jmp':
                tempinstructions[i] = ['nop', argument]
            else:  # if nop
                tempinstructions[i] = ['jmp', argument]
            accumulator, exitcode = oneVisit(tempinstructions)

        i -= 1
    print(i + 1, instructions[i+1])
    return accumulator


def main(day):
    data = aocinput(day)
    instructions = [[part1, int(part2)] for line in data for part1, part2 in [line.strip().split(' ')]]
    result, _ = oneVisit(instructions)
    result2 = findBrokenInstruction(instructions)
    print(result, result2)


if __name__ == '__main__':
    main(8)
