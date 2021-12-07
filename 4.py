def get_empty_board():
    return [[None for _ in range(5)] for _ in range(5)]

numbers_list = None
all_boards = []

with open('project_files/4_puzzle1.txt', 'r') as f:
    board_row = 0
    board_count = 0
    is_first_row = True
    while True:
        line = f.readline()
        if not line:
            break

        if is_first_row:
            line_split = line.strip().split(',')
            numbers_list = [int(num) for num in line_split]
            is_first_row = False
            continue

        if board_row == 0:
            all_boards.append(get_empty_board())

        line_split = line.strip().split()
        if len(line_split) == 0:
            continue
        all_boards[board_count][board_row] = [int(num) for num in line_split]

        if board_row == 4:
            board_row = 0
            board_count += 1
        else:
            board_row += 1

all_boards = all_boards[:100]

import numpy as np

matrix = np.array(all_boards)
marks = np.zeros(matrix.shape)

winning_board = None
winning_number = None
for num in numbers_list:
    mask = matrix == num
    marks = marks + mask

    cols_sum = np.max(np.sum(marks, axis=1), axis=1)
    rows_sum = np.max(np.sum(marks, axis=2), axis=1)
    winning_board_cols = np.where(cols_sum == 5)
    winning_board_rows = np.where(rows_sum == 5)
    if len(winning_board_cols[0]) == 1:
        winning_board = winning_board_cols[0][0]
        winning_number = num
        break
    if len(winning_board_rows[0]) == 1:
        winning_board = winning_board_rows[0][0]
        winning_number = num
        break

print("Solution puzzle 1: ", winning_number * np.sum(matrix[winning_board,:,:] * (marks[winning_board,:,:] == 0)))

matrix = np.array(all_boards)
marks = np.zeros(matrix.shape)
winning_board = None
winning_number = None
for num in numbers_list:
    mask = matrix == num
    marks = marks + mask

    cols_sum = np.max(np.sum(marks, axis=1), axis=1)
    rows_sum = np.max(np.sum(marks, axis=2), axis=1)
    cols_sum_mask = cols_sum < 5
    rows_sum_mask = rows_sum < 5
    boards_mask = np.logical_and(cols_sum_mask, rows_sum_mask)
    if np.sum(boards_mask) == 1 and winning_board == None:
        winning_board = np.where(boards_mask)[0][0]
    if np.sum(boards_mask) == 0:
        winning_number = num
        break

print(winning_board, winning_number)
print("Solution puzzle 2: ", winning_number * np.sum(matrix[winning_board,:,:] * (marks[winning_board,:,:] == 0)))
