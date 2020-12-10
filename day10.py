from inputreader import aocinput


def findDifferences(data):
    data = [int(line) for line in data]
    data = sorted(data + [0, max(data) + 3])
    diff = [data[i] - data[i-1] for i in range(1, len(data))]

    # each length of consecutive diff 1 subsequences gives a number of possible arrangements
    # diff 3 gives only one possible arrangement and limits the subsequences of diff 1
    arrCounter = ArrangementCounter()
    totalArrangements = 1
    count = 1  # start at 1 since there is always at least 1 in a row
    for i in range(1, len(diff)):
        if diff[i] == diff[i-1] == 1:  # don't count consecutive sequences of 3s
            count += 1
        else:
            totalArrangements *= arrCounter.get(count)
            count = 1

    return diff.count(1) * diff.count(3), totalArrangements


class ArrangementCounter:  # cache already calculated arrangement counts
    def __init__(self):
        self._arrangements = {}

    def get(self, n):
        if n not in self._arrangements:
            self._arrangements[n] = self._findArrangements(n)
        return self._arrangements[n]

    def _findArrangements(self, n, tot=0):
        if tot > n:
            return 0
        if tot == n:
            return 1
        return sum([self._findArrangements(n, tot + x) for x in [1, 2, 3]])


def main(day):
    data = aocinput(day)
    result = findDifferences(data)
    print(result)


if __name__ == '__main__':
    main(10)
