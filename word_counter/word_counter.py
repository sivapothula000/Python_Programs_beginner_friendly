import string
import tkinter as tk
from tkinter import messagebox

def count_words():
    sentence = entry.get()
    
    if not sentence.strip():
        messagebox.showwarning("Input Error", "Please enter a sentence!")
        return
    
    words = sentence.split()
    words_count = {}

    for word in words:
        processed_word = word.strip(string.punctuation).lower()
        if processed_word:
            if processed_word in words_count:
                words_count[processed_word] += 1
            else:
                words_count[processed_word] = 1

    # Display result
    output_text.delete("1.0", tk.END)
    for word, count in words_count.items():
        output_text.insert(tk.END, f"{word} : {count}\n")

# GUI setup
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")

tk.Label(root, text="Enter a sentence:", font=("Arial", 12)).pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Count Words", command=count_words).pack(pady=10)

output_text = tk.Text(root, height=10, width=45)
output_text.pack(pady=5)

root.mainloop()
