import tkinter as tk
import numpy
from tkinter import messagebox

# Initialize the game board and symbols
board_size = 5  # Size of the board
board = numpy.array([['_'] * board_size for _ in range(board_size)])  # Create a 5x5 board
player1 = 'X'  # Player 1 symbol
player2 = 'O'  # Player 2 symbol

# Function to check if a player has won by completing a row
def check_rows(symbol):
    for r in range(board_size):
        count = 0
        for c in range(board_size):
            if board[r][c] == symbol:
                count += 1
        if count == board_size:
            return True
    return False

# Function to check if a player has won by completing a column
def check_columns(symbol):
    for c in range(board_size):
        count = 0
        for r in range(board_size):
            if board[r][c] == symbol:
                count += 1
        if count == board_size:
            return True
    return False

# Function to check if a player has won by completing a diagonal
def check_diagonals(symbol):
    # Check the first diagonal (top-left to bottom-right)
    if all(board[i][i] == symbol for i in range(board_size)):
        return True
    # Check the second diagonal (top-right to bottom-left)
    if all(board[i][board_size - i - 1] == symbol for i in range(board_size)):
        return True
    return False

# Function to check if a player has won by any means
def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonals(symbol)

# Function to check if the board is full (draw condition)
def is_draw():
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == '_':
                return False
    return True

# Function to place a symbol on the board
def place(symbol, row, col, button):
    if board[row][col] == '_':
        board[row][col] = symbol
        button.config(text=symbol, state="disabled")

        if won(symbol):
            messagebox.showinfo("Game Over", f"Player {1 if symbol == player1 else 2} ({symbol}) Wins!")
            disable_all_buttons()
            return True

        if is_draw():
            messagebox.showinfo("Game Over", "Match is Draw!")
            disable_all_buttons()
            return True
    return False

# Function to disable all buttons
def disable_all_buttons():
    for row in range(board_size):
        for col in range(board_size):
            buttons[row][col].config(state="disabled")

# Function to reset the game board for a new game
def reset_game():
    global board, current_player
    board = numpy.array([['_'] * board_size for _ in range(board_size)])
    current_player = player1

    for row in range(board_size):
        for col in range(board_size):
            buttons[row][col].config(text="_", state="normal")

# Function to handle the human player's turn
def human_turn(row, col):
    global current_player
    if place(current_player, row, col, buttons[row][col]):
        return

    # Switch to the next player
    current_player = player2 if current_player == player1 else player1

# Create the main window
root = tk.Tk()
root.title(f"Tic-Tac-Toe ({board_size}x{board_size})")

# Create a 5x5 grid of buttons
buttons = [[None for _ in range(board_size)] for _ in range(board_size)]
for row in range(board_size):
    for col in range(board_size):
        buttons[row][col] = tk.Button(
            root, text="_", font="Arial 12", width=5, height=2,
            command=lambda row=row, col=col: human_turn(row, col)
        )
        buttons[row][col].grid(row=row, column=col)

# Button to reset the game
reset_button = tk.Button(root, text="Restart Game", font="Arial 14", command=reset_game)
reset_button.grid(row=board_size, column=0, columnspan=board_size)

# Initial player
current_player = player1

# Run the main loop
root.mainloop()
