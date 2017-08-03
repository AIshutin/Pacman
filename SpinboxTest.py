from tkinter import *
 
root = Tk()
c = Canvas(bg='grey80')
c.pack()
ap = PhotoImage(file = "apple.png")

def _square(self, x, y, d, tag):
    width = 10
    self.create_line(x, y, x + d, y, width = width, tag = tag)
    self.create_line(x, y, x, y + d, width = width, tag = tag)    
    self.create_line(x + d, y, x + d, y + d, width = width, tag = tag)
    self.create_line(x, y + d, x + d, y + d, width= width, tag = tag)
    self.create_image(x, y, anchor = "nw", image = ap, tag = tag)
Canvas.square = _square

def sq1(event):
	print(event)
	print(str(event)[26:])
	print(str(event)[26:].replace("=", ""))
	print(str(event)[26:].replace("=", "").replace("y", ""))
	x, y = map(int, str(event)[26:].replace("=", "").replace("y", "")[:-1].split())
	print(str((x - 1) // 100))
	c.delete("sq" + str((x - 1) // 100))
	c.create_text(30, 10, text = "!!!", anchor = "w", tag = "sq")

c.square(2, 2, 100, "sq1")
c.tag_bind("sq1", "<Button-1>", sq1)
c.square(200, 200, 100, "sq2")
c.tag_bind("sq2", "<Button-1>", sq1)
root.mainloop()