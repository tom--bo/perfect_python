import tkinter as tk

root = tk.Tk()
entry = tk.Entry()
entry.bind('<Return>', lambda e: print(entry.get()))

button = tk.Button(text="Push Me!", command=root.quit)
button.pack()
entry.pack()

root.mainloop()

