import numpy as np   # Importing numpy for array handling
import tkinter as tk
from tkinter import messagebox

# Initialize an empty 3x3 board using numpy array
board = np.array([['_','_','_'],['_','_','_'],['_','_','_']])

player1 = 'X'  # Player 1 symbol is 'X'
player2 = 'O'  # Player 2 symbol is 'O'
current_player = player1  # Start with player X

# Main window creation
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

buttons = [[None for _ in range(3)] for _ in range(3)]  # 2D list for buttons

# Function to check if a player has won by completing a row
def check_rows(symbol):
    for r in range(3):  # Loop through each row
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            return True
    return False

# Function to check if a player has won by completing a column
def check_columns(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            return True
    return False

# Function to check if a player has won by completing a diagonal
def check_diagonals(symbol):
    # Check the first diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbol:
        return True
    # Check the second diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        return True
    return False

# Function to check if a player has won by any means (rows, columns, or diagonals)
def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonals(symbol)

# Function to check if the match is draw
def is_draw():
    for row in board:
        if '_' in row:
            return False
    return True

# Function that runs when a button is clicked (instead of typing row & column)
def on_click(r, c):
    global current_player
    
    # Check if the selected cell is empty
    if board[r][c] == '_':
        board[r][c] = current_player  # Place the symbol on board
        buttons[r][c].config(text=current_player)  # Update the button text
        
        # Check if current player has won
        if won(current_player):
            messagebox.showinfo("Game Over", f"{current_player} Wins!")
            reset_game()
        
        # Check if match is draw
        elif is_draw():
            messagebox.showinfo("Game Over", "Match is Draw!")
            reset_game()
        
        # Switch player turn
        else:
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

# Function to reset the game board
def reset_game():
    global board, current_player
    board = np.array([['_','_','_'],['_','_','_'],['_','_','_']])
    current_player = player1
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="")

# Creating the 3x3 button grid (interface)
for r in range(3):
    for c in range(3):
        btn = tk.Button(
            root,
            text="",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda r=r, c=c: on_click(r, c)  # Passing row & column
        )
        btn.grid(row=r, column=c)
        buttons[r][c] = btn

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, pady=10)

# Start the GUI loop
root.mainloop()
