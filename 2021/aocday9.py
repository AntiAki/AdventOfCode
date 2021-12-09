from time import perf_counter


def process_input_file():
    array = []
    for line in open("inputs/adventofcode9.txt"):
        row = [int(val) for val in line.rstrip("\n")]
        array.append(row)

    find_low_points(array)


def is_low_point(point, frame):
    frame_size = sum([len(row) for row in frame])

    def find_point():
        for j in range(frame_size):
            row = [block[0] for block in frame[j]]
            if "x" in row:
                index = row.index("x")
                return j, index

    y, x = find_point()
    higher = []
    for i in [-1, 1]:
        if 0 <= x + i < len(frame[y]):
            block = frame[y][x + i]
            if block[0] > point:
                higher.append(block)
        if 0 <= y + i < len(frame):
            block = frame[y + i][x]
            if block[0] > point:
                higher.append(block)

    len1 = len(higher)
    if frame_size == 4 and len1 == 2:
        return True, higher
    elif frame_size == 6 and len1 == 3:
        return True, higher
    elif frame_size == 9 and len1 == 4:
        return True, higher
    return False, higher


def create_frame(array, len_array, len_row, x, y):
    frame = []
    for i in range(y - 1 if y != 0 else y, y + 2 if y != len_array - 1 else y + 1):
        frame.append([[array[i][j], (i, j)] if x != j or y != i else ["x", (i, j)]
                      for j in range(x - 1 if x != 0 else x, x + 2 if x != len_row - 1 else x + 1)])
    return frame


def find_basin_size(array, higher, basin_points):
    len_array = len(array)
    len_row = len(array[0])
    new_higher = []
    for high in higher:
        y = high[1][0]
        x = high[1][1]
        frame = create_frame(array, len_array, len_row, x, y)
        point = array[y][x]
        low_point, up = is_low_point(point, frame)
        new_higher.extend([high for high in up if high[0] < 9 and high[1] not in basin_points])
        s = [high[1] for high in new_higher if high[0] < 9]
        basin_points.extend(s)

    if new_higher:
        find_basin_size(array, new_higher, basin_points)
    return list(set(basin_points))


def find_low_points(array):
    low_points = []
    low_point_coords = []
    len_array = len(array)
    basins = []
    for y in range(len_array):
        len_row = len(array[y])
        for x in range(len_row):
            frame = create_frame(array, len_array, len_row, x, y)
            point = array[y][x]
            low_point, higher = is_low_point(point, frame)
            if low_point:
                low_points.append(point + 1)
                low_point_coords.append((y, x))
                higher = [high for high in higher if high[0] < 9]
                basin_points = [high[1] for high in higher if high[0] < 9]
                basin_points.append((y, x))
                size = find_basin_size(array, higher, basin_points)
                basins.append(size)
    print(sum(low_points))

    sorted_basins_slice = sorted(basins, key=len, reverse=True)[0:3]
    total = 1
    for basin in sorted_basins_slice:
        total = total * len(basin)
    print(total)


if __name__ == '__main__':
    t = perf_counter()
    process_input_file()
    print(perf_counter() - t)
