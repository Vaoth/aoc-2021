import os
from collections import defaultdict

def find_common_bits(lines, starting_bit=0, scan_all_bits=True):
    bits = defaultdict(lambda: 0)
    for line in lines:
        for bit in range(starting_bit, len(line)-1):
            bits[bit] += 1 if int(line[bit]) == 1 else -1
            if not scan_all_bits:
                break
    return bits

def find_rating(lines, lcb, mcb):
    for bit in range(len(lines[0])-1):
        bits = find_common_bits(lines, starting_bit=bit, scan_all_bits=False)
        chosen_bit = mcb if int(bits[bit]) >= 0 else lcb
        lines = [line for line in lines if int(line[bit]) == chosen_bit]
        if len(lines) == 1:
            return lines[0]

def find_ratings(lines):
    oxygen_generator_rating = find_rating(lines, 1, 0)
    co2_scrubber_rating = find_rating(lines, 0, 1)

    return int(oxygen_generator_rating, 2), int(co2_scrubber_rating, 2)

def solve(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, name)

    oxygen_generator_rating = 0
    co2_scrubber_rating = 0

    with open(filename) as f:
        lines = f.readlines()
        bits = find_common_bits(lines)
        oxygen_generator_rating, co2_scrubber_rating = find_ratings(lines)
        f.close()
    
    gamma_rate = ''
    for v in bits.values():
         gamma_rate += '1' if v >= 0 else '0'
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = gamma_rate ^ 0xFFF

    return gamma_rate * epsilon_rate, oxygen_generator_rating * co2_scrubber_rating


if __name__ == '__main__':
    print('Result: ' + str(solve('day3.txt')))