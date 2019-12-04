from time import time
from utils import read_input


def problem_a(wires):
    c = Circuit(wires)
    c.read_wiring()
    c.dedupe_paths()
    c.find_all_intersections()
    c.find_shortest_intersections()
    return c.shortest_distance


def problem_b(wires):
    c = Circuit(wires)
    c.read_wiring()
    c.dedupe_paths()
    c.find_all_intersections()
    c.find_nearest_intersections()
    return c.shortest_path


class Circuit:
    def __init__(self, instructions):
        self.instructions = instructions

        self.board = []
        self.dedepud_board = []
        self.current_location = [0, 0]

        self.intersections = None
        self.shortest_distance = None
        self.shortest_path = None

    def read_wiring(self):
        for i, instruction in enumerate(self.instructions):
            self.current_location = [0, 0]
            self.board.append([])
            for step in instruction:
                self.walk_path(step, i)

    def parse_path(self, route):
        direction = route[0:1]
        distance = int(route[1:])
        return direction, distance

    def walk_path(self, instruction, path_idx):
        drct, dist = self.parse_path(instruction)
        for i in range(dist):
            if drct == 'U':
                self.current_location[1] += 1
            elif drct == 'D':
                self.current_location[1] -= 1
            elif drct == 'R':
                self.current_location[0] += 1
            elif drct == 'L':
                self.current_location[0] -= 1
            self.board[path_idx].append(self.current_location[:])

    def dedupe_paths(self):
        for path in self.board:
            self.dedepud_board.append(set([tuple(x) for x in path]))

    def find_all_intersections(self):
        # Find all coordinates where both paths meet
        self.intersections = self.dedepud_board[0] & self.dedepud_board[1]

    def find_shortest_intersections(self):
        # Convert back to list
        intersections = [list(x) for x in self.intersections]
        # Make all values absolute
        for i, intersection in enumerate(intersections):
            intersections[i] = sum([abs(intersections[i][0]), abs(intersections[i][1])])

        self.shortest_distance = min(intersections)

    def find_nearest_intersections(self):
        total_distances = []
        for i in self.intersections:
            a = self.board[0].index(list(i))
            b = self.board[1].index(list(i))
            total_distances.append(a + b)
        self.shortest_path = min(total_distances) + 2


# puz = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
#        ['U62','R66','U55','R34','D71','R55','D58','R83']]
#
# puz = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
#        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]


if  __name__ == '__main__':
    s = time()
    puzzle_input = read_input('day3.txt').split('\n')
    puzzle_input = [x.split(',') for x in puzzle_input]

    print(f"Solution for Part A: {problem_a(puzzle_input)}")
    print(f"Solution for Part B: {problem_b(puzzle_input)}")
    print(f"Completed in {time()-s:.4f} seconds")
