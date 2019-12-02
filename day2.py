from time import time
from utils import read_input


def problem_a(intcode):
    intcode[1] = 12
    intcode[2] = 2
    output = opcode_processor(intcode[:])
    return output[0]


def problem_b(intcode):
    for noun in range(1, 100):
        for verb in range(1, 100):
            intcode[1] = noun
            intcode[2] = verb
            output = opcode_processor(intcode[:])
            if output[0] == 19690720:
                print(f"Noun: {noun}\nVerb: {verb}")
                return 100 * noun + verb
    raise ValueError()


def opcode_processor(arr):
    idx = 0
    while idx <= len(arr):
        if arr[idx] == 1:
            arr[arr[idx+3]] = arr[arr[idx+1]] + arr[arr[idx+2]]
        elif arr[idx] == 2:
            arr[arr[idx+3]] = arr[arr[idx+1]] * arr[arr[idx+2]]
        elif arr[idx] == 99:
            return arr
        else:
            raise ValueError

        idx += 4
    raise ValueError


def test_a():
    assert opcode_processor([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == \
           [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert opcode_processor([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert opcode_processor([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert opcode_processor([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert opcode_processor([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


if __name__ == '__main__':
    s = time()
    puzzle_input = read_input('day2.txt').split(',')
    puzzle_input = [int(x) for x in puzzle_input]

    print(f"Solution for Part A: {problem_a(puzzle_input)}")
    print(f"Solution for Part B: {problem_b(puzzle_input)}")
    print(f"Completed in {time()-s:.4f} seconds")
