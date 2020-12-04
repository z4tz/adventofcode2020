from inputreader import aocinput
from typing import List, Tuple


def validPassports(data: List[str]) -> Tuple[int, int]:
    fieldValidators = {'byr': lambda x: x.isnumeric() and 2002 >= int(x) >= 1920,
                       'iyr': lambda x: x.isnumeric() and 2020 >= int(x) >= 2010,
                       'eyr': lambda x: x.isnumeric() and 2030 >= int(x) >= 2020,
                       'hgt': hgtValid,
                       'hcl': hclValid,
                       'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                       'pid': lambda x: x.isnumeric() and len(x) == 9
                       }

    entries = ''.join([line.replace('\n', ' ') for line in data]).split('  ')
    part1 = 0
    part2 = 0
    for entry in entries:
        if sum([fieldname in entry for fieldname in fieldValidators.keys()]) == 7:
            part1 += 1

            # if entry has required fields, validate field data for part 2
            for item in entry.split(' '):
                parts = item.split(':')
                if parts[0] == 'cid':  # no validation on cid
                    continue
                if not fieldValidators[parts[0]](parts[1]):
                    break
            else:  # all validation passed
                part2 += 1

    return part1, part2


def hgtValid(height: str) -> bool:
    try:
        if height.endswith('cm'):
            if 193 >= int(height[:-2]) >= 150:
                return True
        elif height.endswith('in'):
            if 76 >= int(height[:-2]) >= 59:
                return True
    except ValueError:
        pass
    return False


def hclValid(color: str) -> bool:
    if color.startswith('#'):
        try:
            int(color[1:], 16)
            return True
        except ValueError:
            pass
    return False


def main(day):
    data = aocinput(day)
    result = validPassports(data)
    print(result)


if __name__ == '__main__':
    main(4)
