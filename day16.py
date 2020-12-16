from inputreader import aocinput
from typing import List, Set
from functools import reduce


class Field:
    def __init__(self, name: str, validValues: Set[int]):
        self.name = name
        self.validValues = validValues
        self.position = None
        self.possiblePositions = set(range(20))

    def positionNotPossible(self, position):
        try:
            self.possiblePositions.remove(position)
        except KeyError:
            pass

    def __repr__(self):
        return f'{self.name} - positions: {self.position}'


def ticketErrorRate(data: List[str]):
    i = 0
    limits = set()
    fields = {}
    while data[i].strip():
        name, limit = data[i].split(':')
        values = set()
        for part in limit.split('or'):
            numbers = part.split('-')
            values.update(range(int(numbers[0]), int(numbers[1]) + 1))
        limits.update(values)
        fields[name] = Field(name, values)

        i += 1
    myticket = [int(value) for value in data[i+2].split(',')]

    i += 5
    tickets = [[int(number) for number in line.split(',')] for line in data[i:]]
    part1 = sum([number for ticket in tickets for number in ticket if not int(number) in limits])

    validTickets = []
    for ticket in tickets:
        for value in ticket:
            if value not in limits:
                break
        else:
            validTickets.append(ticket)

    for ticket in validTickets:
        for position, value in enumerate(ticket):
            for field in fields.values():
                if value not in field.validValues:
                    field.positionNotPossible(position)

    for _ in range(len(ticket)):
        for field in fields.values():
            if len(field.possiblePositions) == 1:
                position = field.possiblePositions.pop()
                field.position = position
                for tempfield in fields.values():
                    tempfield.positionNotPossible(position)

    part2 = reduce(lambda x, y: x*y, [myticket[field.position] for field in fields.values() if 'departure' in field.name])


    return part1, part2



def main(day):
    data = aocinput(day)
    result = ticketErrorRate(data)
    print(result)


if __name__ == '__main__':
    main(16)
