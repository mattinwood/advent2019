from time import time
from utils import read_input


def fuel_requirements(mass: int) -> int:
    '''
    :param mass: The mass of the input for which to calculate fuel for
    :return: The fuel required for the given mass.
    '''
    return (int(mass) // 3) - 2


def problem_a() -> int:
    '''
    Read the list of all module masses for input, and run the non-recursive function for determining fuel requirements.
    :return: The total fuel requirements of all modules.
    '''
    modules = read_input('day1.txt')
    fuel = [fuel_requirements(x) for x in modules]
    return sum(fuel)


def recursive_fuel_requirements(mass: int) -> int:
    '''
    :param mass: The mass of the input for which to calculate fuel for
    :return: The fuel required for the given mass, as well as fuel required for the additional fuel.
    '''
    fuel = (int(mass)//3) - 2
    # Any mass of 6 or less functionally requires zero fuel, and thus does not require any add'l fuel
    if fuel > 6:
        fuel += recursive_fuel_requirements(fuel)
    return fuel


def problem_b() -> int:
    '''
    Read the list of all module masses for input, and run the recursive function for determining fuel requirements.
    :return: The total fuel requirements of all modules, as well as the fuel requirements for the fuel.
    '''
    modules = read_input('day1.txt')
    fuel = [recursive_fuel_requirements(x) for x in modules]
    return sum(fuel)


def test_fuel_requirements():
    assert fuel_requirements(12) == 2
    assert fuel_requirements(14) == 2
    assert fuel_requirements(1969) == 654
    assert fuel_requirements(100756) == 33583


def test_total_fuel_requirements():
    assert recursive_fuel_requirements(14) == 2
    assert recursive_fuel_requirements(1969) == 966
    assert recursive_fuel_requirements(100756) == 50346


if __name__ == '__main__':
    s = time()
    print(f"Solution for Part A: {problem_a()}")
    print(f"Solution for Part B: {problem_b()}")
    print(f"Completed in {time()-s:.4f} seconds")
