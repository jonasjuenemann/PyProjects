import pygame
import time
import numpy as np

np.random.seed(1)

# board = np.random.randint(0, 9, size=(9, 9))

p = 0.2  # Anzahl an 0 im Start Soduko

prob = (1 - p) / 9

probs = [p] + [prob] * 9
print(probs)
board = np.random.choice(10, size=(9, 9), p=probs)
print(board)


# print(board.T)


def elimduplicates(board):
    seen_row = {}
    for row_index in range(9):
        seen_row[row_index] = set()
        for col_index in range(9):
            if board[row_index][col_index] != 0:
                while board[row_index][col_index] in seen_row[row_index]:
                    board[row_index][col_index] = np.random.randint(1, 10)
                seen_row[row_index].add(board[row_index][col_index])
    print(board)
    board = board.T
    print(seen_row)
    # print(board)
    for col_index in range(9):
        seen_col = set()
        for row_index in range(9):
            if board[col_index][row_index] != 0:
                num = 1
                while board[col_index][row_index] in seen_col:
                    if num not in seen_row[row_index]:
                        board[col_index][row_index] = num
                    num += 1
                    if num == 10:
                        # Hier kommt der Algorithmus nicht mehr weiter, muesste jetzt die vorherigen Reihen checken, was da zu aendern ist.
                        board[col_index][row_index] = 0
                        print("Array not solvable at Point board[" + str(col_index) + "][" + str(row_index) + "], 0 added")
                        # raise Exception("Array not solvable at Point board[" + str(col_index) + "]["+ str(row_index) + "]")
                if board[col_index][row_index] != 0:
                    seen_col.add(board[col_index][row_index])
                    seen_row[row_index].add(board[col_index][row_index])


elimduplicates(board)
print(board)


"""Solveable Board:

"""