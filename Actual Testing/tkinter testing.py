import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Greeter")
root.geometry("300x150")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

btn = tk.Button(root, text="Greet", command=greet)
btn.pack()

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()