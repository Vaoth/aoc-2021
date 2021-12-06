import os

def simulate(fish, days, new_fish_timer=8, reset_fish_timer=6):
    fish = [fish.count(i) for i in range(new_fish_timer + 1)]
    for day in range(days):
        print(fish)
        new_fish = fish[0]
        fish[0:new_fish_timer] = fish[1:new_fish_timer + 1]
        fish[reset_fish_timer] += new_fish
        fish[new_fish_timer] = new_fish
    return sum(fish)

def solve(name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, name)

    fish = [int(f) for f in open(filepath).read().split(',')]

    return simulate(fish, 80), simulate(fish, 256)

if __name__ == '__main__':
    print("Result: " + str(solve("day6.txt")))