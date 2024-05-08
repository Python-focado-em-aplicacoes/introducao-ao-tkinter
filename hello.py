import tkinter
from tkinter import ttk, Tk

root = Tk()

frame = ttk.Frame(root, padding=10)
frame.grid()

label = ttk.Label(frame, text="Hello world").grid(row=0, column=0)

exit_button = ttk.Button(frame, text="Sair", command=root.destroy).grid(row=1, column=0)

root.geometry("800x600")

icon = tkinter.PhotoImage(file="./python_real.png")
root.iconphoto(True, icon)

root.mainloop()