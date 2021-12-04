def avg(lst):
    return sum(lst) / len(lst)


def process_input(filename, part2=False):
    input_lst = []
    for n, row in enumerate(open(filename)):
        binary_string = row.strip("\n")

        if part2:
            input_lst.append(binary_string)
        else:
            for i in range(0, len(binary_string)):
                if n == 0:
                    input_lst.append([int(binary_string[i])])
                else:
                    input_lst[i].append(int(binary_string[i]))

    return input_lst


def get_most_or_least_common(lst, index, least_common=False):
    sub_list = []
    for i in range(0, len(lst)):
        binary_string = lst[i]
        sub_list.append(binary_string[index])

    if least_common:
        return "1" if sub_list.count("1") >= sub_list.count("0") else "0"
    else:
        return "1" if sub_list.count("1") < sub_list.count("0") else "0"


def aocd31(input_lst):
    binary_string = ''.join([str(round(avg(item))) for item in input_lst])
    flipped_binary = ''.join(["1" if i == "0" else "0" for i in binary_string])

    print(int(binary_string, 2) * int(flipped_binary, 2))


def aoc32(input_lst):
    oxygen_list = input_lst
    co2_list = input_lst

    for i in range(0, len(str(input_lst[0]))):
        oxygen_list_common = get_most_or_least_common(oxygen_list, i)
        co2_list_least_common = get_most_or_least_common(co2_list, i, least_common=True)

        if len(oxygen_list) > 1:
            oxygen_list = [v for v in oxygen_list if v[i] == oxygen_list_common]
        if len(co2_list) > 1:
            co2_list = [v for v in co2_list if v[i] == co2_list_least_common]

    print(int(oxygen_list[0], 2) * int(co2_list[0], 2))


if __name__ == '__main__':
    inputfile = 'inputs/adventofcode3.txt'
    processed_input = process_input(inputfile)
    aocd31(processed_input)

    part2_processed_input = process_input(inputfile, part2=True)
    aoc32(part2_processed_input)
