from collections import defaultdict

# Configuration for different kind of fish :D
CONFIG = {"cycle": "6", "birth": "8"}


def initialize_fish():
    initial_lanternfish = [int(fish) for fish in open("inputs/adventofcode6.txt").readline().split(",")]
    initial_counts = defaultdict(int)
    for fish in initial_lanternfish:
        key = str(fish)
        initial_counts[key] += 1

    return initial_lanternfish, initial_counts


# recursively grow list of all fish
def simulate_lanternfish(lanternfish_list, days):
    new_fish = []

    for fish in lanternfish_list:
        if fish == 0:
            new_fish.extend([int(CONFIG["cycle"]), int(CONFIG["birth"])])
        else:
            new_fish.append(fish - 1)
    if days != 1:
        return simulate_lanternfish(new_fish, days - 1)
    else:
        return new_fish


# Instead of growing a huge list, recursively manage only counts
def dynamic_simulate_lanternfish(counts, days):
    new_counts = defaultdict(int)
    for i in sorted([int(key) for key in counts.keys()]):
        dict_key = str(i)
        if i == 0:
            new_counts[CONFIG["birth"]] = counts[dict_key]
            new_counts[CONFIG["cycle"]] = counts[dict_key]
        else:
            new_counts[str(i - 1)] += counts[dict_key]

    if days != 1:
        return dynamic_simulate_lanternfish(new_counts, days - 1)
    else:
        return sum(new_counts.values())


if __name__ == '__main__':
    init_fish, init_count = initialize_fish()
    print(len(simulate_lanternfish(init_fish, 80)))  # part1 solution
    print(dynamic_simulate_lanternfish(init_count, 256))  # part2 solution
