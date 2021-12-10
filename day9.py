import os

def solve(name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, name)

    points = []
    with open(filepath) as f:
        lines = f.readlines()
        points = [[int(p) for p in line.strip()] for line in lines]
        f.close()

    lowest_points = []
    basin_sizes = []
    for y, line in enumerate(points):
        for x, point in enumerate(line):
            shifts = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            get_point = lambda y, x, s: points[y + s[1]][x + s[0]] if (len(points) > y + s[1] >= 0) and (len(line) > x + s[0] >= 0) else 10
            get_coors = lambda y, x, s: [y + s[1], x + s[0]] if (len(points) > y + s[1] >= 0) and (len(line) > x + s[0] >= 0) else [-1,-1]
            neighbours = [get_point(y, x, s) for s in shifts]
            if all(point < n for n in neighbours):
                print(point, neighbours)
                lowest_points.append(point)

                basin = [[y,x]]
                for j, i in basin:
                    basin += [get_coors(j, i, s) for s in shifts if get_point(j, i, s) != 9 and get_coors(j, i, s) not in basin]
                basin = [b for b in basin if -1 not in b]
                basin_sizes.append(len(basin))

    risk_levels = [n + 1 for n in lowest_points]
    basin_sizes.sort()
    basin_product = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

    return sum(risk_levels), basin_product

if __name__ == '__main__':
    print("Result: " + str(solve("day9.txt")))