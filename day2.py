import os

def solve(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, name)

    horizontal = 0
    depth = 0
    aim = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            args = line.split()
            command = args[0]
            print(args)
            if command == 'forward':
                horizontal += int(args[1])
                depth += aim * int(args[1])
            elif command == 'down':
                aim += int(args[1])
            elif command == 'up':
                aim -= int(args[1])
        f.close()
    print(horizontal, depth)
    return horizontal * depth

if __name__ == '__main__':
    print('Result: ' + str(solve('day2.txt')))