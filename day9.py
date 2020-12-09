from inputreader import aocinput


def notXmas(data, preamble=25):
    data = [int(line) for line in data]
    for i in range(len(data)-preamble):
        for j in range(i, i + preamble):
            if (data[i+preamble] - data[j]) in data[i:i+preamble] and (data[i+preamble] - 2 * data[j]) != 0:
                break
        else:
            part1 = data[i+preamble]

    i = 0
    j = 2
    contset = sum(data[i:j])
    while contset != part1:
        if contset > part1:
            i += 1
        else:
            j += 1
        contset = sum(data[i:j])
    return part1, min(data[i:j]) + max(data[i:j])


def main(day):
    data = aocinput(day)
    result = notXmas(data)
    print(result)


if __name__ == '__main__':
    main(9)
