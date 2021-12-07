import os
from numpy import *

product_of_sums = lambda a: a * (a + 1) // 2

def get_optimum_fuel(positions, increasing_fuel):
    if not increasing_fuel:
        return int(sum(abs(positions - median(positions))))
    else:
        lower_bound = sum(product_of_sums(abs(positions - floor(mean(positions)))))
        upper_bound = sum(product_of_sums(abs(positions - ceil(mean(positions)))))
        return int(min(lower_bound, upper_bound))

def solve(name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, name)

    positions = [int(pos) for pos in open(filepath).read().split(',')]
    
    return get_optimum_fuel(positions, False), get_optimum_fuel(positions, True)

if __name__ == '__main__':
    print("Result: " + str(solve("day7.txt")))