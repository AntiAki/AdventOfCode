from time import perf_counter


def part_1():
    outputs = []
    for line in open("inputs/adventofcode8.txt"):
        line = line.rstrip("\n").split(" | ")
        output = line[1].split(" ")
        outputs.extend([len(digit) for digit in output])

    print(len([output for output in outputs if output in [2, 3, 4, 7]]))


def part_2():
    ans_sum = 0
    for line in open("inputs/adventofcode8.txt"):
        line = line.rstrip("\n").split(" | ")
        ipt = line[0].split(" ")
        output = line[1].split(" ")
        ans_sum += decoder(ipt, output)
    print(ans_sum)


def decoder(ipt, output):
    dt = {}
    set_segments = [set(segments) for segments in ipt]
    for segments in [segs for segs in set_segments if len(segs) in [2, 3, 4, 7]]:
        if len(segments) == 2:
            dt[1] = segments
        if len(segments) == 3:
            dt[7] = segments
        if len(segments) == 4:
            dt[4] = segments
        if len(segments) == 7:
            dt[8] = segments
        set_segments.remove(segments)

    while len(dt.keys()) != 9:
        for segments in set_segments:
            if len(segments) == 6 and len(dt.keys()) <= 6:
                difference = segments.symmetric_difference(dt[8])
                if difference.issubset(dt[1]):
                    dt[6] = segments
                elif difference.issubset(dt[4]) and not difference.issubset(dt[7]):
                    dt[0] = segments
                elif len(dt.keys()) == 6:
                    dt[9] = segments

            if len(segments) == 5 and len(dt.keys()) > 6:
                if len(dt.keys()) == 7:
                    dt[5] = dt[6].intersection(dt[9])
                elif segments.issubset(dt[9]) and segments != dt[5]:
                    dt[3] = segments

    for segments in set_segments:
        if segments not in dt.values():
            dt[2] = segments
            break

    num_list = []
    for segments in output:
        for key, value in dt.items():
            if value == set(segments):
                num_list.append(key)
                break

    return int(''.join([str(num) for num in num_list]))


if __name__ == '__main__':
    part_1()
    t = perf_counter()
    part_2()
    print(perf_counter() - t)
