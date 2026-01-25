import tkinter as tk
from tkinter import messagebox

def calculate_flames():
    name1 = entry1.get().lower().replace(" ", "")
    name2 = entry2.get().lower().replace(" ", "")

    if not name1 or not name2:
        messagebox.showwarning("Input Error", "Please enter both names!")
        return

    n1 = list(name1)
    n2 = list(name2)

    # Removing common letters
    for i in n1[:]:
        for j in n2[:]:
            if i == j:
                n1.remove(i)
                n2.remove(j)
                break

    count = len(n1) + len(n2)

    result = ['F','L','A','M','E','S']

    while len(result) > 1:
        split_index = count % len(result) - 1
        if split_index < 0:
            split_index = len(result) - 1
        result = result[split_index+1:] + result[:split_index]

    flames_map = {
        'F': "Friends",
        'L': "Love",
        'A': "Affection",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings"
    }

    final_result = flames_map[result[0]]
    messagebox.showinfo("FLAMES Result", f"Relationship: {final_result}")

# GUI setup
root = tk.Tk()
root.title("FLAMES Game")
root.geometry("400x250")

tk.Label(root, text="Enter Your Name:", font=("Arial", 12)).pack(pady=5)
entry1 = tk.Entry(root, width=30)
entry1.pack()

tk.Label(root, text="Enter Crush Name:", font=("Arial", 12)).pack(pady=5)
entry2 = tk.Entry(root, width=30)
entry2.pack()

tk.Button(
    root,
    text="Calculate FLAMES",
    font=("Arial", 12),
    bg="green",        # background color
    fg="white",        # text color
    activebackground="darkgreen",
    command=calculate_flames
).pack(pady=20)

root.mainloop()
