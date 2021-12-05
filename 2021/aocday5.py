from collections import Counter
from time import time


class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.orientation = self.determine_and_fix_orientation()
        self.list_rep = self.list_representation()

    def determine_and_fix_orientation(self):
        if self.start[1] == self.end[1]:
            if self.end[0] < self.start[0]:
                end = self.end
                self.end = self.start
                self.start = end
            return "x"
        elif self.start[0] == self.end[0]:
            if self.end[1] < self.start[1]:
                end = self.end
                self.end = self.start
                self.start = end
            return "y"
        else:
            if self.end[0] < self.start[0]:
                end = self.end
                self.end = self.start
                self.start = end
            return "d"

    def get_points(self):
        return self.start, self.end

    def get_orientation(self):
        return self.orientation

    def list_representation(self):
        match self.orientation:
            case "x":
                return [(self.start[0] + i, self.start[1]) for i in range((self.end[0] - self.start[0]) + 1)]
            case "y":
                return [(self.start[0], self.start[1] + i) for i in range((self.end[1] - self.start[1]) + 1)]
            case "d":
                return [(self.start[0] + i, self.start[1] + i if self.end[1] > self.start[1] else self.start[1] - i)
                        for i in range((self.end[0] - self.start[0]) + 1)]


def create_lines():
    lines = []
    for line in open("inputs/adventofcode5.txt"):
        line_coordinate_strings = line.strip("\n").split(" -> ")
        start_points = line_coordinate_strings[0].split(",")
        end_points = line_coordinate_strings[1].split(",")
        lines.append(Line((int(start_points[0]), int(start_points[1])), (int(end_points[0]), int(end_points[1]))))

    return lines


def count_intersections(lines):
    all_line_points = []
    for line in lines:
        all_line_points.extend(line.list_rep)

    counts = Counter(all_line_points)
    duplicates = [point for point in all_line_points if counts[point] > 1]
    print(len(set(duplicates)))


if __name__ == '__main__':
    t = time()
    count_intersections(create_lines())
    print(time() - t)
