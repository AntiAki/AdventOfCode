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


def count_fish(counts):
    new_counts = defaultdict(int)
    for i in sorted([int(key) for key in counts.keys()]):
        dict_key = str(i)
        if i == 0:
            new_counts[CONFIG["birth"]] = counts[dict_key]
            new_counts[CONFIG["cycle"]] = counts[dict_key]
        else:
            new_counts[str(i - 1)] += counts[dict_key]
    return new_counts


# recursively grow list of all fish
def recursive_simulate_lanternfish(lanternfish_list, days):
    if days != 0:
        new_fish = []
        for fish in lanternfish_list:
            if fish == 0:
                new_fish.extend([int(CONFIG["cycle"]), int(CONFIG["birth"])])
            else:
                new_fish.append(fish - 1)
        return recursive_simulate_lanternfish(new_fish, days - 1)
    else:
        return len(lanternfish_list)


# Instead of growing a huge list, recursively manage only counts
def dynamic_recursive_simulate_lanternfish(counts, days):
    if days != 0:
        new_counts = count_fish(counts)
        return dynamic_recursive_simulate_lanternfish(new_counts, days - 1)
    else:
        return sum(counts.values())


def dynamic_simulate_lantern_fish_iterative(counts, days):
    for i in range(0, days):
        new_counts = count_fish(counts)
        counts = new_counts
    return sum(counts.values())


if __name__ == '__main__':
    init_fish, init_count = initialize_fish()
    print(recursive_simulate_lanternfish(init_fish, 80))  # part1 solution
    print(dynamic_recursive_simulate_lanternfish(init_count, 256))  # part2 solution, limited to max recursion depth
    print(dynamic_simulate_lantern_fish_iterative(init_count, 256))  # part2 iterative solution, no limits
