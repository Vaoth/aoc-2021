import os
from collections import defaultdict
import numpy as np

def connect(ends):
    delta = np.diff(ends, axis=0)[0]
    delta_max = np.argmax(np.abs(delta))
    delta_absolute = np.abs(delta[delta_max])
    positions = np.arange(delta_absolute + 1)
    result = ends[0] + (np.outer(positions, delta) + (delta_absolute >> 1)) // delta_absolute
    return result

def solve(name):
    dirpath = os.path.dirname(__file__)
    filepath = os.path.join(dirpath, name)

    vents = []
    with open(filepath) as f:
        lines = f.readlines()
        vents = [[[int(n) for n in args.split(',')] for args in line.strip().split(' -> ')] for line in lines]
        f.close()

    vent_lines = defaultdict(lambda: 0)
    for vent in vents:
        positions = connect(vent)
        for x, y in positions:
            vent_lines[x, y] += 1

    intersections = [(k,v) for k, v in vent_lines.items() if v >= 2]
    return len(intersections)

if __name__ == '__main__':
    print("Result: " + str(solve("day5.txt")))