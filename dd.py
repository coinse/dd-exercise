import math
from problem import execute_input

def read_input(filename):
    """ Reads the input stored in filename """
    f = open(filename, "r")
    seq = [int(line.strip()) for line in f.readlines()]
    return seq

def check_error(seq):
    """ 
    This function simulates the error checking.
    It will return True if the given sequence still fails the test.
    """
    try:
        execute_input(seq)
    except RuntimeError:
        return True
    return False

def dd():
    """ 
    Implements the linear, recursive delta debugging.
    Note that the function signature is intentionally incomplete
    (i.e., you need to provide arguments yourself)
    """

if __name__ == '__main__':
    seq = read_input("fail.txt")
    print(check_error(seq))
    minimised = dd(seq)
    print(check_error(minimised), minimised)