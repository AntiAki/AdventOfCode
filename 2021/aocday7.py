from collections import defaultdict, Counter
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
        for key, item in horizontal_position_counts.items():
            if i == 0:
                fuel_min += consumption_lookup[abs(i - key)] * item
            else:
                fuel += consumption_lookup[abs(i - key)] * item
                if fuel > fuel_min:
                    break
        if fuel < fuel_min and i != 0:
            fuel_min = fuel
    print(fuel_min)


if __name__ == '__main__':
    t = perf_counter()
    dynamic()
    print(perf_counter() - t)
