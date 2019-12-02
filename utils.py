def read_input(filename) -> list:
    '''
    :param filename: The name of the file in format day{x}.txt where {x} is the day of the challenge
    :return: List of values for the problem set
    '''
    return open('inputs/' + filename, 'r').read().split('\n')