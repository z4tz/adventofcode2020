from inputreader import aocinput


def findSum(data: list, target: int):
    prevJ = len(data)-1
    for i, entry in enumerate(data):
        for j in range(prevJ, 0, -1):
            if entry + data[j] == target:
                return entry * data[j]
            elif entry + data[j] < target:
                break
        prevJ = j


def findTripleSum(data: list, target: int):
    for i, entry in enumerate(data):
        for j, entry2 in enumerate(data[i+1:]):
            for entry3 in data[j+1:]:
                entrysum = entry + entry2 + entry3
                if entrysum == target:
                    return entry * entry2 * entry3
                if entrysum > target:
                    break


def main(day):
    data = aocinput(day)
    data = sorted([int(item) for item in data])
    result = findSum(data, 2020), findTripleSum(data, 2020)
    print(result)


if __name__ == '__main__':
    main(1)
