from inputreader import aocinput
from typing import List
import regex


def ruleParser(line: str) -> int or List[List[int]]:
    if '\"' in line:
        return line.replace('\"', '')
    return [[int(num) for num in part.split(' ') if num] for part in line.split('|')]


ruleDict = {}


def expandRule(item):
    if type(item) is str:
        return item
    options = []
    for option in item:
        if -1 in option:  # rule 8
            return f'({expandRule(ruleDict[option[0]])})+'
        elif -2 in option:  # rule 11
            return f'(?P<self>({expandRule(ruleDict[option[0]])})(?&self)?({expandRule(ruleDict[option[2]])}))'
        else:
            options.append(''.join([expandRule(ruleDict[part]) for part in option]))
    return r'({})'.format('|'.join(options))


def matchRules(data: List[str]):
    ruleDict.update({int(part[0]): ruleParser(part[1].strip()) for line in data[:data.index('\n')] for part in [line.split(':')]})
    messages = [line.strip() for line in data[data.index('\n') + 1:]]

    compiled = regex.compile(fr'^{expandRule(ruleDict[0])}$')
    count = sum([bool(compiled.match(message)) for message in messages])

    ruleDict[8][0].append(-1)
    ruleDict[11][0].insert(1, -2)
    compiled = regex.compile(fr'^{expandRule(ruleDict[0])}$')
    count2 = sum([bool(compiled.match(message)) for message in messages])
    return count, count2


def main(day):
    data = aocinput(day)
    result = matchRules(data)
    print(result)


if __name__ == '__main__':
    main(19)
