from tkinter import *
root = Tk()
a = StringVar()
a.set("2")
sp = Spinbox(values = ("1", '2', '3', '4', '5'), textvariable = a)
sp.pack()
bt = Button(text = "PRESS", command = lambda: print(a, a.get()))
bt.pack()
root.mainloop()