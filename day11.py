from inputreader import aocinput


def occupiedSeats(data):
    def neighbors(y, x):
        count = 0
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            j = x + dx
            i = y + dy

            if 0 <= i < ymax and 0 <= j < xmax:
                if seats[i][j] == '#':
                    count += 1
        return count

    seats = [[char for char in line.strip()] for line in data]
    previousOccupied = -1
    occupiedCount = 0
    ymax, xmax = len(seats), len(seats[0])

    while previousOccupied != occupiedCount:
        newSeats = []
        for y in range(ymax):
            row = []
            for x in range(xmax):
                if seats[y][x] == '.':  # skip over empty floor
                    row.append('.')
                else:
                    count = neighbors(y, x)
                    if seats[y][x] == 'L' and count == 0:
                        row.append('#')
                    elif seats[y][x] == '#' and count >= 4:
                        row.append('L')
                    else:
                        row.append(seats[y][x])
            newSeats.append(row)

        seats = newSeats
        previousOccupied = occupiedCount
        occupiedCount = sum(seat == '#' for row in seats for seat in row)

    return occupiedCount


def occupied2(data):

    def neighbors(y, x):
        count = 0
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            ytemp = y + dy
            xtemp = x + dx
            while 0 <= ytemp < ymax and 0 <= xtemp < xmax:
                seat = seats[ytemp][xtemp]
                if seat == '#':
                    count += 1
                    break
                if seat == 'L':
                    break
                xtemp += dx
                ytemp += dy
        return count

    seats = [[char for char in line.strip()] for line in data]
    previousOccupied = -1
    occupiedCount = 0
    ymax, xmax = len(seats), len(seats[0])

    while previousOccupied != occupiedCount:
        newSeats = []
        for y in range(ymax):
            row = []
            for x in range(xmax):
                if seats[y][x] == '.':  # skip over empty floor
                    row.append('.')
                else:
                    count = neighbors(y, x)
                    if seats[y][x] == 'L' and count == 0:
                        row.append('#')
                    elif seats[y][x] == '#' and count >= 5:
                        row.append('L')
                    else:
                        row.append(seats[y][x])
            newSeats.append(row)

        seats = newSeats
        previousOccupied = occupiedCount
        occupiedCount = sum(seat == '#' for row in seats for seat in row)
    return occupiedCount


def main(day):
    data = aocinput(day)
    result = occupiedSeats(data)
    result2 = occupied2(data)
    print(result, result2)


if __name__ == '__main__':
    main(11)
