def show_array(array):
    for row in array:
        print(' '.join([str(num) for num in row]))


def show_frame(frame):
    if len(frame) % 3 == 0 and len(frame) % 6 == 0:
        for s in range(0, len(frame), 3):
            print(' '.join([str(i) for i in frame[s:s + 3]]))
    else:
        for s in range(0, len(frame), 2):
            print(' '.join([str(i) for i in frame[s:s + 2]]))


def is_low_point(point, frame):
    def clean_frame(ix):
        if type(ix) != list:
            frame.pop(ix)
        else:
            for i in sorted(ix, reverse=True):
                frame.pop(i)
        frame.remove("x")

    index = frame.index("x")
    len_frame = len(frame)
    low_point = False
    if len_frame == 4:
        if index == 0:
            clean_frame(3)
        elif index == 1:
            clean_frame(2)
        elif index == 2:
            clean_frame(1)
        elif index == 3:
            clean_frame(0)

    elif len_frame == 6:
        if index == 1:
            clean_frame([3, 5])
        elif index == 2:
            clean_frame([1, 5])
        elif index == 3:
            clean_frame([0, 4])
        elif index == 4:
            clean_frame([0, 2])

    elif len_frame == 9:
        clean_frame([0, 2, 6, 8])

    if point < min(frame):
        low_point = True

    return low_point


def find_low_points(array):
    low_points = []
    len_array = len(array)
    for y in range(len_array):
        len_row = len(array[y])
        for x in range(len_row):
            frame = []
            for i in range(y - 1 if y != 0 else y, y + 2 if y != len_array - 1 else y + 1):
                for j in range(x - 1 if x != 0 else x, x + 2 if x != len_row - 1 else x + 1):
                    frame.append(array[i][j] if x != j or y != i else "x")
            point = array[y][x]
            if is_low_point(point, frame):
                low_points.append(point+1)

    print(sum(low_points))
def process_input_file():
    array = []
    for line in open("inputs/adventofcode9.txt"):
        row = [int(val) for val in line.rstrip("\n")]
        array.append(row)

    # show_array(array)
    find_low_points(array)


if __name__ == '__main__':
    process_input_file()
