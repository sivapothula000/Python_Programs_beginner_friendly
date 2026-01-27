import tkinter as tk
from tkinter import messagebox

# Function to generate magic square 
def magic_square(n):
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)

    i = n // 2
    j = n - 1
    num = n * n
    count = 1

    while count <= num:
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if magicSquare[i][j] != 0:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[i][j] = count
            count += 1

        i = i - 1
        j = j + 1

    return magicSquare

# Generate UI grid
def generate_magic_square():
    try:
        n = int(entry.get())

        if n % 2 == 0:
            messagebox.showerror("Error", "Enter an ODD number only!")
            return

        result = magic_square(n)

        # Clear old grid
        for widget in grid_frame.winfo_children():
            widget.destroy()

        # Create new grid
        for i in range(n):
            for j in range(n):
                lbl = tk.Label(
                    grid_frame,
                    text=str(result[i][j]),
                    font=("Arial", 14, "bold"),
                    width=5,
                    height=2,
                    relief="solid",
                    bg="white"
                )
                lbl.grid(row=i, column=j, padx=2, pady=2)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

# Main window
root = tk.Tk()
root.title("Magic Square Generator")
root.geometry("500x500")

# Top input section
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Enter an odd number (n):", font=("Arial", 12)).pack(side="left")
entry = tk.Entry(top_frame, width=5)
entry.pack(side="left", padx=5)

tk.Button(
    top_frame,
    text="Generate",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=generate_magic_square
).pack(side="left", padx=10)

# Grid frame
grid_frame = tk.Frame(root)
grid_frame.pack(pady=20)

root.mainloop()
