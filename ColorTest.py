from tkinter import *
Tk()
def _normalize(self): # Make Canvas normal size #ToDo
    print(self)
    z = self.bbox(ALL)
    print(z)
    a, b, c, d = z[0], z[1], z[2], z[3]
    print(a, b, c, d)
    self.config(height = abs(a - c), width = abs(b - d))
Canvas.normalize = _normalize

def _square(self, x, y, d): #Special method to draw square
    width = 5
    self.create_line(x, y, x + d, y, width = width) # tag = tag
    self.create_line(x, y, x, y + d, width = width)    
    self.create_line(x + d, y, x + d, y + d, width = width)
    self.create_line(x, y + d, x + d, y + d, width= width)
Canvas.square = _square    

c = Canvas(bg = "white", width = 500, height = 500)
c.pack()
c.square(0, 0, 100)
c.normalize()
mainloop()