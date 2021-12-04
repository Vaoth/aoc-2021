import os

def solve(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, name)

    increments = 0
    with open(filename) as f:
        lines = f.readlines()
        previous_sum = 0
        for i in range(3, len(lines), 1):
            sum = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
            if i > 3:
                eval = sum > previous_sum
                increments += 1 if eval else 0
                print(lines[i-2].rstrip() + '+' + lines[i-1].rstrip() + '+' + lines[i].rstrip() + '=' + str(sum) + (' (increased)' if eval else ' (decreased)'))
            previous_sum = sum
        f.close()
    return increments

if __name__ == '__main__':
    print('Result: ' + str(solve('day1.txt')))