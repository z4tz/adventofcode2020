from inputreader import aocinput
from collections import Counter


def groupCounts(data):
    groups = [line.replace('\n', '') for line in ''.join(data).split('\n\n')]
    counts = sum([len(set(group)) for group in groups])
    return counts


def allYes(data):
    yesCount = 0
    for group in (''.join(data).split('\n\n')):
        persons = group.count('\n')+1
        counter = Counter(group)
        yesCount += list(counter.values()).count(persons)
    return yesCount


def main(day):
    data = aocinput(day)
    result = groupCounts(data)
    result2 = allYes(data)
    print(result, result2)


if __name__ == '__main__':
    main(6)
