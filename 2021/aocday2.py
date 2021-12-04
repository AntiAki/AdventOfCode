def process_input(name):
    f = open(name, 'r')
    li = []
    for row in f:
        row = row.replace("\n", "")
        li.append(row)
    return li


def d2aoc1(li):
    horizontal_position = 0
    vertical_position = 0
    for i in li:
        v = int(i[-1])
        if i[0] == "f":
            horizontal_position += v
        elif i[0] == "u":
            vertical_position -= v
        else:
            vertical_position += v

    print(horizontal_position * vertical_position)


def d2aoc2(li):
    horizontal_position = 0
    vertical_position = 0
    aim = 0
    for i in li:
        v = int(i[-1])
        if i[0] == "f":
            horizontal_position += v
            vertical_position += aim * v
        elif i[0] == "u":
            aim -= v
        else:
            aim += v

    print(horizontal_position * vertical_position)


def d2aoc22():
    h = a = d = 0
    for i in open("inputs/adventofcode2.txt"):
        match i.strip("\n").split():
            case "forward", n:
                h += int(n)
                d += int(n) * a
            case "down", n:
                a += int(n)
            case "up", n:
                a -= int(n)
    print(a * h, h * d)


if __name__ == '__main__':
    list_input = process_input('inputs/adventofcode2.txt')
    # d2aoc1(list_input)
    d2aoc22()
