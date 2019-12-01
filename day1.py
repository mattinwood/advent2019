from time import time


def read_input(filename):
    return open(filename, 'r').read().split('\n')


def fuel_req(m):
    return (int(m)//3) - 2


def problem_a():
    mass = read_input('inputs/day1.txt')
    mass = [fuel_req(x) for x in mass]
    return sum(mass)


def recursive_fuel_req(m):
    f = (int(m)//3) - 2
    if f > 6:
        f += recursive_fuel_req(f)
    return f


def problem_b():
    mass = read_input('inputs/day1.txt')
    mass = [recursive_fuel_req(x) for x in mass]
    return sum(mass)


if __name__ == '__main__':
    s = time()
    print(f"Solution for Part A: {problem_a()}")
    print(f"Solution for Part B: {problem_b()}")
    print(f"Completed in {time()-s} seconds")
