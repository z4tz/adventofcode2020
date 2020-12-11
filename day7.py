from inputreader import aocinput
from typing import List, Tuple


class Bag:
    def __init__(self, color):
        self.color = color
        self._Contain = {}
        self._contentOf = set()

    def addContent(self, bag, count) -> None:
        bag.addContentOf(self)
        self._Contain[bag] = count

    def addContentOf(self, bag) -> None:
        self._contentOf.add(bag)

    def contains(self) -> dict:
        return self._Contain

    def containedIn(self) -> set:
        return self._contentOf

    def __repr__(self):
        return f'Bag object with color:{self.color}'


allBags = {}


def getBag(bagColor: str) -> Bag:
    if bagColor in allBags:
        return allBags[bagColor]
    else:
        bag = Bag(bagColor)
        allBags[bagColor] = bag
        return bag


def countBags(bag: Bag) -> int:
    return sum([countBags(containedBag) * count for containedBag, count in bag.contains().items()]) + 1


def containsBag(data: List[str]) -> Tuple[int, int]:
    for line in data:
        container, contains = line.strip().split('contain')
        containerColor = ' '.join(container.split(' ')[0:2])
        bag = getBag(containerColor)

        if 'no other bag' in contains:  # bag does not contain further bags
            continue
        for contain in contains.split(','):
            count, *color, _ = contain.strip().split(' ')  # color contains two parts, adjective and the color
            bag.addContent(getBag(' '.join(color)), int(count))

    # part 1
    bagQueue = [getBag('shiny gold')]
    canHoldGold = set()
    while bagQueue:
        tempBags = bagQueue.pop().containedIn()
        bagQueue.extend(tempBags)
        canHoldGold.update(tempBags)

    # part 2
    bagCount = countBags(getBag('shiny gold')) - 1

    return len(canHoldGold), bagCount


def main(day):
    data = aocinput(day)
    result = containsBag(data)
    print(result)


if __name__ == '__main__':
    main(7)
