from tkinter import *
from win32api import GetSystemMetrics
from time import*
import subprocess

class prec:
    def __init__(self, width, height, version, source):
        self.width = width
        self.height = height
        self.version = version
        self.source = source

def _square(self, x, y, d):
    width = 2
    self.create_line(x, y, x + d, y, width = width)
    self.create_line(x, y, x, y + d, width = width)    
    self.create_line(x + d, y, x + d, y + d, width = width)
    self.create_line(x, y + d, x + d, y + d, width= width)
Canvas.square = _square    

def _wall(self, x, y, d):
    width = 2
    self.square(x, y, d)
    self.create_line(x, y, x + d, y + d, width = width)
    self.create_line(x + d, y, x, y + d, width = width)
    self.create_line(x + d // 2, y, x + d / 2, y + d, width = width)
    self.create_line(x, y + d // 2, x + d, y + d // 2, width = width)
Canvas.wall = _wall

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
Canvas.create_circle = _create_circle

def _food(self, x, y, d):
    #global c
    self.square(x, y, d)
    self.create_circle(x + d // 2, y + d // 2, d // 4, width = 2)
Canvas.food = _food

def _stuf(self, x, y, d, gif1):
    #global c
    #gif1 = PhotoImage(file='pacman.gif')
    self.square(x, y, d)
    self.create_image(x, y, image=gif1, anchor=NW)  
Canvas.stuf =_stuf

def _draw_gamefield(self, curr):   
    h = len(curr)
    w = len(curr[0])
    w_r = settings.width / w
    h_r = settings.height / h
    d = min(w_r, h_r)
    w_r = d
    h_r = d
    for i in range(h):
        for j in range(w):
            x = j * w_r
            y = i * h_r
            if (h > w):
                x, y = y, x
            if curr[i][j] == "0":
                self.wall(x, y, d)
            if curr[i][j] == ".":
                self.food(x, y, d)
            if curr[i][j] == "<":
                self.stuf(x, y, d, pc)
            if curr[i][j] == "a":
                self.stuf(x, y, d, ap)
            if curr[i][j] == "c":
                self.stuf(x, y, d, ch)
Canvas.draw_gamefield = _draw_gamefield

def CreateGameField():
    cmd = 'helper.bat'
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
    while True:
        try:
            z = open("sys")
            if z.readline().rstrip() == '1':
                z.close()
                break
            z.close()
        except:
            sleep(1)
            break
    fin = open(settings.source)
    arr = fin.readlines() + ['\n']
    fin.close()
    curr = []
    arr += ['\n']
    for el in arr:
        if el.rstrip() == "":
            if len(curr) == 0:
                continue
            #print(curr)
            #print(arr)
            return curr
        curr.append(el.rstrip())

def destroy(obj):
    #print(obj)
    if (not obj):
        return
    try:
        #print(winfo_children())
        if obj.winfo_children():
            for el in obj.winfo_children():
                destroy(el)
    except:
        pass
    try:
        frm.pack_forget()
    except:
        pass
    try: 
        obj.destroy()
    except:
        return


class screen:
    """docstring for  screen"""
    def __init__(self):
        self.window = []
        self.sp = []
        self.error = []

    def add(self, arg):
        self.window.append(arg)
    
    def add_sp(self, arg):
        self.add(arg)
        self.sp.append(arg)
    
    def add_es(self, arg):
        self.add(arg)
        self.error = arg

    def remove(self):
        for el in self.window:
            destroy(el)
        self.window = []
        self.sp = []
        self.error = []

def menu_game():
    app.remove()
    fr = Frame(bg = "black")
    fr.pack()
    lb = Label(fr, text = "Please, wait.")
    lb.pack()
    root.update()
    curr = CreateGameField()
    lb.destroy()
    c = Canvas(fr, width = settings.width, height = settings.height, bg = "white")
    c.pack(expand=YES, fill=BOTH)   
    c.draw_gamefield(curr)
    app.add(c)
    app.add(fr)
    bt = Button(root, text = "Back", command = menu_settings)
    bt.pack()
    app.add(bt)
    app.add(fr)

def Quit():
    exit(0)

def ChangeSettings():
    menu_game()
    pass

def Error():
    pass

def com():
    arr = []
    log = 0
    valide = ["3", "6", "9", "12", "15", "18", "21", "24"]
    for el in app.sp:
        z = el.get()
        if z not in valide:
            log = 1
        arr.append(el.get())
    if log == 1:
        Error()
    else:
        ChangeSettings()

def menu_settings():
    app.remove()
    fr = Frame(root)
    fr.pack()
    app.add(fr)
    lb = Label(fr, text = "Width: ")
    lb.grid(row = 1, column = 1)
    app.add(lb)
    sc = Spinbox(fr, values = (3, 6, 9, 12, 15, 18, 21, 24))
    sc.grid(row = 1, column = 2)
    app.add_sp(sc)
    bt = Button(fr, text = "Start Menu", command = menu_start)
    bt.grid(row = 2, column = 1)
    app.add(bt)
    bt1 = Button(fr, text = "Next", command = com)
    bt1.grid(row = 2, column = 2)
    app.add(bt1)

def menu_start():
    app.remove()
    fr = Frame(bg = "blue")
    fr.pack()
    bt = Button(fr, text = "New game", command = menu_settings)
    bt.pack()
    bt1 = Button(fr, text = "Quit", command = Quit)
    bt1.pack()
    app.add(fr)
    app.add(bt)
    app.add(bt1)
   
fin = open("settings.txt")
data = fin.readlines()
source = data[-1].rstrip()
fin.close()
settings = prec(GetSystemMetrics(0) - 115, GetSystemMetrics(1) - 140, "3.3 alfa", source) #-15, -40
root = Tk()
app = screen()
pc = PhotoImage(file='pacman.gif') 
ap = PhotoImage(file='apple.png') 
ch = PhotoImage(file='cherry.png')   
root.title("Pacman v" + str(settings.version))
root.geometry(str(settings.width) + 'x' + str(settings.height))
menu_start()
root.mainloop()