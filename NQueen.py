import tkinter as tk

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens(n):
    def solve_recursively(board, row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                if solve_recursively(board, row + 1):
                    return True
                board[row][col] = 0
        return False

    board = [[0] * n for _ in range(n)]
    if solve_recursively(board, 0):
        return board
    else:
        return None