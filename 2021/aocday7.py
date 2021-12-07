from collections import defaultdict, Counter
from math import ceil, floor
from statistics import mean, median
from time import perf_counter


def naive():
    numbers = [int(num) for num in open("inputs/adventofcode7.txt").readline().split(",")]

    fuel_sums = [0 for i in range(min(numbers), max(numbers))]
    for i in range(len(fuel_sums)):
        for num in numbers:
            fuel_sums[i] += sum([i for i in range(1, abs(i - num) + 1)])
    print(min(fuel_sums))


def dynamic():
    numbers = [int(num) for num in open("inputs/adventofcode7.txt").readline().split(",")]

    horizontal_position_counts = Counter(numbers)

    consumption_lookup = defaultdict(int)
    for i in range(min(numbers) + 1, max(numbers) + 1):
        consumption_lookup[i] = consumption_lookup[i - 1] + i

    fuel_min = 0
    for i in range(min(numbers), max(numbers)):
        fuel = 0
        for h_pos, count in horizontal_position_counts.items():
            if i == 0:
                fuel_min += consumption_lookup[abs(i - h_pos)] * count
            else:
                fuel += consumption_lookup[abs(i - h_pos)] * count
                if fuel > fuel_min:
                    break
        if fuel < fuel_min and i != 0:
            fuel_min = fuel
    print(fuel_min)


def part_1_median():
    numbers = [int(num) for num in open("inputs/adventofcode7.txt").readline().split(",")]
    num_median = int(median(numbers))
    print(sum([abs(num - num_median) for num in numbers]))


# Thanks, Luca
def part_2_mean():
    numbers = [int(num) for num in open("inputs/adventofcode7.txt").readline().split(",")]
    num_mean = mean(numbers)
    ceil_sum = sum([sum([i for i in range(0, abs(ceil(num_mean) - num) + 1)]) for num in numbers])
    floor_sum = sum([sum([i for i in range(0, abs(floor(num_mean) - num) + 1)]) for num in numbers])
    print(min([ceil_sum, floor_sum]))


if __name__ == '__main__':
    part_1_median()
    t = perf_counter()
    part_2_mean()  # Maths
    print(perf_counter() - t)
    t = perf_counter()
    dynamic()
    print(perf_counter() - t)