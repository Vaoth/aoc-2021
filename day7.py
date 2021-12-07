import os
from numpy import *

sum_of_n = lambda n: n * (n + 1) // 2

def get_optimum_fuel(positions, increasing_fuel):
    if not increasing_fuel:
        return int(sum(abs(positions - median(positions))))
    else:
        lower_bound = sum(sum_of_n(abs(positions - floor(mean(positions)))))
        upper_bound = sum(sum_of_n(abs(positions - ceil(mean(positions)))))
        return int(min(lower_bound, upper_bound))

def solve(name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, name)

    positions = [int(pos) for pos in open(filepath).read().split(',')]
    
    return get_optimum_fuel(positions, False), get_optimum_fuel(positions, True)

if __name__ == '__main__':
    print("Result: " + str(solve("day7.txt")))