
def process_input(name):
    f = open(name, 'r')
    li = []
    for row in f:
        row = int(row.strip("\n"))
        li.append(row)
    return li


def aoc1(li):
    c = 0
    for i in range(0, len(li) - 1):
        if li[i] < li[i + 1]:
            c += 1
    print(c)


def aoc2(li):
    c = 0
    for i in range(0, len(li) - 3):
        fs = li[i:i + 3]
        ss = li[i + 1:i + 4]
        if sum(ss) > sum(fs) and len(ss) == 3:
            c += 1
    print(c)


# Two middle numbers are actually unnecessary
def aoc2_alt(li):
    c = 0
    for i in range(0, len(li) - 3):
        if li[i + 3] > li[i]:
            c += 1
    print(c)


# Python style answer
def aoc2_alt2(li):
    print(sum([1 if li[i + 3] > li[i] else 0 for i in range(0, len(li) - 3)]))


if __name__ == '__main__':
    list_input = process_input('inputs/adventofcode1.txt')
    aoc1(list_input)
    aoc2(list_input)
    aoc2_alt(list_input)
    aoc2_alt2(list_input)
