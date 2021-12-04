def process_input(file_name):
    f = open(file_name, "r")
    li = []
    for row in f:
        li.append(int(row.replace("\n","")))

    return li


def aoc1(li):

    for i in li:
        for a in li:
            for b in li:
                if i+a+b == 2020:
                    return i*a*b



if __name__ == '__main__':
    list_input = process_input("inputs/adventofcode1.txt")
    print(aoc1(list_input))