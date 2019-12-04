from time import time
from utils import read_input


def problem_a(password_range):
    validations = []
    for p in range(password_range[0], password_range[1]):
        validations.append(validate_password(p))
    return sum(validations)


def problem_b(password_range):
    validations = []
    for p in range(password_range[0], password_range[1]):
        validations.append(validate_password(p, part_b=True))
    return sum(validations)


def parse_input(s):
    return [int(s.split('-')[0]), int(s.split('-')[1])]


def validate_password(password, part_b=False):
    parsed_pass = [int(i) for i in str(password)]

    ascending = parsed_pass == sorted(parsed_pass[:])
    if not ascending:
        return False

    counts = {}
    for digit in parsed_pass:
        counts[digit] = counts.get(digit, 0) + 1

    if part_b:
        return 2 in list(counts.values())
    else:
        return max(list(counts.values())) >= 2


if __name__ == '__main__':
    s = time()
    puzzle_input = read_input('day4.txt').split(',')[0]
    puzzle_input = parse_input(puzzle_input)

    print(f"Solution for Part A: {problem_a(puzzle_input)}")
    print(f"Solution for Part B: {problem_b(puzzle_input)}")
    print(f"Completed in {time()-s:.4f} seconds")
