import tkinter as tk

def printen():
    print("Hallo")

fenster = tk.Tk()
fenster.geometry("500x200")
knopf = tk.Button(fenster, text="Printen", command=printen, width=10, height=5)
knopf.pack()

fenster.mainloop()