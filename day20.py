from inputreader import aocinput
import numpy as np
from collections import defaultdict
from functools import reduce
import math


def matchingEdge(image1, image2):
    for edge1 in [image1[0, :], image1[-1, :], image1[:, 0], image1[:, -1]]:
        for edge2 in [image2[0, :], image2[-1, :], image2[:, 0], image2[:, -1]]:
            if (edge1 == edge2).all() or (edge1 == np.flip(edge2)).all():
                return True
    return False


def orientImage(edge, image2):
    for _ in range(4):
        if (edge == image2[:, 0]).all():
            return image2
        elif (edge == np.flipud(image2[:, 0])).all():
            return np.flipud(image2)
        image2 = np.rot90(image2)
    return None


def findCorners(data):
    images = {}
    for i in range(0, len(data), 12):
        id = int(data[i][5:-2])
        images[id] = np.array([[char == '#' for char in line.strip()] for line in data[i + 1:i + 11]])
    matches = defaultdict(list)

    for index, image in enumerate(images.items()):  # image[0] = id and image[1] is image
        for idToMatch, toMatch in list(images.items())[index:]:
            if image[0] != idToMatch and matchingEdge(image[1], toMatch):
                matches[image[0]].append(idToMatch)
                matches[idToMatch].append(image[0])

    part1 = reduce(lambda x, y: x * y, [id for id, matchIDs in matches.items() if len(matchIDs) == 2])

    matchedOrder = []
    combinedWidth = int(math.sqrt(len(images)))

    # get a corner part
    for id, matchIDs in matches.items():
        if len(matchIDs) == 2:
            current = id
            break

    # rotate and flip first two parts to start in top left corner
    toMatchId = matches[current][0]
    image1, image2 = images[current], images[toMatchId]
    orientedImage = orientImage(image1[:, -1], image2)
    while orientedImage is None:
        image1 = np.rot90(image1)
        orientedImage = orientImage(image1[:, -1], image2)

    # orient first two vertically by making sure it's possible to match at bottom of first image
    toMatchVert = matches[current][1]
    if not orientImage(image1[-1, :], images[toMatchVert]):  # if cant match to bottom, flip upside down
        image1 = np.flipud(image1)
        image2 = np.flipud(image2)
    images[current] = image1  # "save" changes after possibly rotating and flipping
    images[toMatchId] = image2
    matchedOrder.extend([current, toMatchId])  # order of first two items

    def removeMatches(id1, id2):  # remove matches to reduce possible options on future matches
        try:
            matches[id1].remove(id2)
            matches[id2].remove(id1)
        except ValueError:
            pass

    removeMatches(current, toMatchId)

    # order first row
    for _ in range(2, combinedWidth):
        current = matchedOrder[-1]

        for toMatchId in matches[current]:
            orientedImage = orientImage(images[current][:, -1], images[toMatchId])
            if orientedImage is not None:
                break
        images[toMatchId] = orientedImage
        matchedOrder.append(toMatchId)
        removeMatches(current, toMatchId)

    # match and order rest by matching below, going left to right
    for i in range(combinedWidth, len(images)):
        current = matchedOrder[i - combinedWidth]
        toMatchId = matches[current][0]  # only one left
        orientedImage = orientImage(images[current][-1, :], images[toMatchId])  # pass bottom
        if orientedImage is None:
            print(f'error, could not orient image{toMatchId} below image {current}')
            exit()
        images[toMatchId] = np.fliplr(
            np.rot90(orientedImage, -1))  # rotate -1 since orientImage matches to the right, not bottom
        matchedOrder.append(toMatchId)
        removeMatches(current, toMatchId)

        # remove match to the left of the newly ordered image
        prevMatchId = matchedOrder[-2]
        removeMatches(prevMatchId, toMatchId)

    for id, image in images.items():
        images[id] = images[id][1:-1, 1:-1]  # crop away edges

    # combine full image
    horiParts = []
    for row in range(combinedWidth):
        horiParts.append(
            np.concatenate([images[id] for id in matchedOrder[row * combinedWidth:(row + 1) * combinedWidth]], axis=1))
    fullimage = np.concatenate(horiParts)

    monster = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    monster = np.array([[char == '#' for char in line] for line in monster])

    class Found(Exception):  # simple exception to break out of nested for loops
        pass

    # look for monster at each possible location, rotation and flip in fullImage
    try:
        for _ in range(2):
            for _ in range(4):
                monsterCount = 0
                for y1, y2 in zip(range(fullimage.shape[0] - monster.shape[0]),
                                  range(monster.shape[0], fullimage.shape[0])):
                    for x1, x2 in zip(range(fullimage.shape[0] - monster.shape[1]),
                                      range(monster.shape[1], fullimage.shape[0])):
                        if np.sum(np.multiply(fullimage[y1:y2, x1:x2], monster)) == 15:
                            monsterCount += 1
                if monsterCount >= 1:
                    raise Found
                fullimage = np.rot90(fullimage)
            fullimage = np.fliplr(fullimage)
    except Found:
        pass
    else:
        print('No monsters found in fullimage')
        exit()

    return part1, np.count_nonzero(fullimage) - monsterCount * 15


def main(day):
    data = aocinput(day)
    result = findCorners(data)
    print(result)


if __name__ == '__main__':
    main(int(__file__.split('/')[-1][3:-3]))
