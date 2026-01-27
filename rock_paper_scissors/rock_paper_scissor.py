import tkinter as tk
from tkinter import messagebox
import random

choices = ["ROCK", "PAPER", "SCISSORS"]

def play(user_choice):
    computer_choice = random.randint(0, 2)

    user_text = choices[user_choice]
    computer_text = choices[computer_choice]

    result_text = f"You chose: {user_text}\nComputer chose: {computer_text}\n\n"

    if user_choice == 0 and computer_choice == 2:
        result_text += "You Win!"
    elif computer_choice > user_choice:
        result_text += "You Lose!"
    elif user_choice == 2 and computer_choice == 0:
        result_text += "You Lose!"
    elif user_choice > computer_choice:
        result_text += "You Win!"
    else:
        result_text += "Match Is Draw!"

    messagebox.showinfo("Result", result_text)

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16, "bold")).pack(pady=20)
tk.Label(root, text="Choose one:", font=("Arial", 12)).pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="ROCK", width=10, height=2,
          command=lambda: play(0)).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="PAPER", width=10, height=2,
          command=lambda: play(1)).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="SCISSORS", width=10, height=2,
          command=lambda: play(2)).grid(row=0, column=2, padx=10)

root.mainloop()
