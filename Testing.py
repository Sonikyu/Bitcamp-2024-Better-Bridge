import tkinter as tk
import tkinter.filedialog

root = tk.Tk("Input Image")
root.withdraw()


filename = tkinter.filedialog.askopenfilename()
print(filename)