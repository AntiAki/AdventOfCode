def process_input(file_name):
    li = []
    for row in open(file_name, "r"):
        row = row.replace("\n", "").replace(":", "")
        split_row = row.split(" ")
        r = split_row[0].split("-")
        char = split_row[1]
        pw = split_row[2]
        li.append({"r": (int(r[0]), int(r[-1])), "c": char, "p": pw})

    return li


def aoc2(li):
    valid_count = 0
    for i in li:
        if i["r"][0] <= i["p"].count(i["c"]) <= i["r"][1]:
            valid_count += 1
    return valid_count


# aoc 2020/2.2
def aoc22(li):
    return sum([1 if any(x) and not all(x) else 0 for x in [[True if i["p"][o - 1] == i["c"] else False for o in [x for x in i["r"]]] for i in li]])


# aoc 2020/2.2, crazy person solution
def aoc222(li):
    return sum(([1 if any(x) and not all(x) else 0 for x in [[True if i["p"][o - 1] == i["c"] else False for o in [x for x in i["r"]]] for i in [{"r": (int(i.split(" ")[0].split("-")[0]), int(i.split(" ")[0].split("-")[1])), "c": i.split(" ")[1][0], "p": i.split(" ")[2].replace("\n", "")} for i in open(
        "inputs/adventofcode2.txt", "r")]]]))


if __name__ == '__main__':
    list_input = process_input("inputs/adventofcode2.txt")
