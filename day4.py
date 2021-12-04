import os
from collections import defaultdict
import functools
import operator

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def visualize_matrix(matrix, view_transpose=False):
    print('================================================================')
    for row in matrix:
        print(row)
    if view_transpose:
        print('\n')
        board_t = transpose(matrix)
        for row in board_t:
            print(row)

def retrieve_boards(lines, length):
    cells = lines.split()
    cells = [int(cell) for cell in cells]
    boards = []
    for i in range(0, len(cells), length * length):
        board = []
        for j in range(0, len(cells[i:i + length * length]), length):
            board.append(cells[i + j:i + j + length])
        boards.append(board)
    return boards

def check_row(counter, board, number, length, b_id, name):
    bingo = False
    for r_id, row in enumerate(board):
        identifier = name + str(r_id)
        if number in set(row):
            counter[b_id][identifier] += 1
            bingo = counter[b_id][identifier] == length
    return counter, bingo

def find_bingo(numbers, boards, length):
    counter = defaultdict(lambda: defaultdict(lambda: 0))
    bingo = False
    for n_id, number in enumerate(numbers):
        for b_id, board in enumerate(boards):
            counter, bingo = check_row(counter, board, number, length, b_id, 'row')
            counter, bingo = check_row(counter, transpose(board), number, length, b_id, 'column')
            if bingo:
                return board, n_id, b_id

def calculate_result(winning_board, numbers, n_id):
    visualize_matrix(winning_board)
    winning_board = functools.reduce(operator.iconcat, winning_board, [])
    winning_board = [number for number in winning_board if number not in numbers[:n_id+1]]
    return sum(winning_board) * numbers[n_id]

def solve(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, name)

    numbers = []
    boards = []
    length = 5
    with open(filename) as f:
        numbers = next(f).strip().split(',')
        numbers = [int(number) for number in numbers]
        lines = f.read().replace('\n', ' ').replace('  ', ' ').replace('  ', ' ')

        boards = retrieve_boards(lines, length)
        f.close()
    
    winning_boards = []
    while len(boards) > 0:
        winning_board, n_id, b_id = find_bingo(numbers, boards, length)
        winning_boards.append([winning_board, n_id])
        boards.pop(b_id)

    first = calculate_result(winning_boards[0][0], numbers, winning_boards[0][1])
    last = calculate_result(winning_boards[-1][0], numbers, winning_boards[-1][1])

    return first, last


if __name__ == '__main__':
    print("Result: " + str(solve('day4.txt')))