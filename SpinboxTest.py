from tkinter import*
def com():
	print(s.get())
root = Tk()
s = Spinbox(values = (3, 6, 9, 12, 15, 18, 21, 24))
s.pack()
bt = Button(text = "Press me", command = com)
bt.pack()
root.mainloop()