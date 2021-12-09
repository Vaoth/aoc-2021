import os
from collections import defaultdict

intersection = lambda l: ''.join(set.intersection(*[set(x) for x in l]))
disjoint = lambda l: ''.join(set.symmetric_difference(*[set(x) for x in l]))
inv_dic = lambda d: {v: k for k, v in d.items()}

def solve(name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, name)

    entries = []
    with open(filepath) as f:
        lines = f.readlines()
        entries = [[[''.join(s) for s in args.split()] for args in line.strip().split(' | ')] for line in lines]
        f.close()

    segments = {'abcefg': '0', 
                'cf': '1', 
                'acdeg': '2', 
                'acdfg': '3',
                'bcdf': '4',
                'abdfg': '5',
                'abdefg': '6',
                'acf': '7',
                'abcdefg': '8',
                'abcdfg': '9'}
    known_unique_lengths = {6: 'b', 4: 'e', 9: 'f'}
    outputs = []
    for entry in entries:
        frequency = defaultdict(lambda: 0)
        equivalents = defaultdict(lambda: '')
        signals = entry[0]
        output = entry[1]
        signals.sort(key = len)

        for d in 'abcdefg':
            frequency[d] = sum(s.count(d) for s in signals)

        one, seven = signals[0], signals[1]
        signals = signals[3:9] #remaining signals to decipher
        signals_five_seg = signals[:3]

        for k, v in frequency.items():
            equivalents[k] = known_unique_lengths[v] if v in known_unique_lengths else ''

        equivalents[disjoint([one, seven])] = 'a'
        equivalents[disjoint([intersection(signals), inv_dic(equivalents)['a']])] = 'g'
        equivalents[disjoint([disjoint([intersection(signals_five_seg), inv_dic(equivalents)['a']]), inv_dic(equivalents)['g']])] = 'd'
        equivalents[''.join([k for k, v in equivalents.items() if not v])] = 'c'
        equivalents = {ord(k): v for k, v in equivalents.items()}
        signals = entry[0]
        output = [''.join(sorted(s.translate(equivalents))) for s in output]
        outputs.append(int(''.join(segments[o] for o in output)))

    return sum(outputs)

    
if __name__ == '__main__':
    print("Result: " + str(solve("day8.txt")))