from aocday3 import process_input



def get_sublist(lst, index):
    sub_list = []
    for i in range(0, len(lst)):
        binary_string = lst[i]
        sub_list.append(binary_string[index])

    return sub_list


def avg(lst):
    return sum(lst) / len(lst)


def aocd31(input_lst):
    print(avg(input_lst[0]))
    binary_string = ''.join([str(round(avg(item))) for item in input_lst])
    flipped_binary = ''.join(["1" if i == "0" else "0" for i in binary_string])

    print(int(binary_string, 2) * int(flipped_binary, 2))


def aoc32(input_lst):
    oxygen_list = input_lst
    co2_list = input_lst

    for i in range(0, len(str(input_lst[0]))):
        oxygen_sublist = get_sublist(oxygen_list, i)
        co2_sublist = get_sublist(co2_list, i)
        oxygen_list_common = "1" if oxygen_sublist.count("1") >= oxygen_sublist.count("0") else "0"
        co2_list_least_common = "1" if co2_sublist.count("1") < co2_sublist.count("0") else "0"

        if len(oxygen_list) > 1:
            oxygen_list = [v for v in oxygen_list if v[i] == oxygen_list_common]
        if len(co2_list) > 1:
            co2_list = [v for v in co2_list if v[i] == co2_list_least_common]

    print(int(oxygen_list[0], 2) * int(co2_list[0], 2))


def aoc32_alt():
    oxygen_list = carbon_list = process_input('inputs/adventofcode31.txt', True)

    for i in range(0, len(oxygen_list[0])):
        sublist = get_sublist(oxygen_list, i)
        most_common = "1" if sublist.count("1") >= len(oxygen_list) / 2 else "0"
        print(most_common)
        if len(oxygen_list) > 1:
            oxygen_list = [value for value in oxygen_list if value[i] == most_common]
    print(oxygen_list[0])

    for i in range(0, len(carbon_list[0])):
        sublist = get_sublist(carbon_list, i)
        count = sublist.count("1")
        floor1 = len(carbon_list) / 2
        least_common = "1" if count < floor1 else "0"
        print(least_common)
        if len(carbon_list) > 1:
            carbon_list = [value for value in carbon_list if value[i] == least_common]
    print(carbon_list[0])

    print(int(carbon_list[0], 2) * int(oxygen_list[0], 2))


if __name__ == '__main__':
    processed_input = process_input('inputs/adventofcode31.txt')
    #aocd31(processed_input)
    part2_processed_input = process_input('inputs/adventofcode31.txt', True)
    aoc32(part2_processed_input)
    #aoc32_alt()
    wrong = ["6153535","5774081"]