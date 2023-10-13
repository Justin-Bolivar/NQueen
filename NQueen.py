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
    

def update_solution_text(board):
    solution_text.config(state=tk.NORMAL)
    solution_text.delete(1.0, tk.END)
    if board is None:
        solution_text.insert(tk.END, "No solution found.")
    else:
        for row in board:
            centered_row = "".join("Q" if x == 1 else "." for x in row)
            space_padding = " " * ((len(board) - len(centered_row)) // 2)
            centered_row = space_padding + centered_row + space_padding
            solution_text.insert(tk.END, centered_row + "\n")
    solution_text.config(state=tk.DISABLED)

def solve_and_display_solution(*args):
    n = int(entry.get())
    final_solution = solve_n_queens(n)
    update_solution_text(final_solution)

window = tk.Tk()
window.title("N-Queens")

label = tk.Label(window, text="Enter Chessboard Size (N):")
label.pack(pady = 10)

entry = tk.Entry(window)
entry.pack(pady = 5)

solve_button = tk.Button(window, text="Solve", command=solve_and_display_solution)
solve_button.pack(pady = 10)

solution_text = tk.Text(window, height=10, width=30, state=tk.DISABLED)
solution_text.pack(pady = 10)

entry.bind('<Return>', solve_and_display_solution)

window.mainloop()