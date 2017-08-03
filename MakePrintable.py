from tkinter import filedialog
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
    w_r = (settings.width - 100) / w
    h_r = (settings.height - 100)/ h
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

def CPacman():
    cmd = 'helper.bat'
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
    z = clock()
    while clock() - z < 1:
        root.update()
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

def CreateGameField(source):
    fin = open(source)
    arr = fin.readlines() + ['\n']
    fin.close()
    curr = []
    arr += ['\n']
    for el in arr:
        if el.rstrip() == "":
            if len(curr) == 0:
                continue
            return curr
        curr.append(el.rstrip())

def GameCreating(source):
    CPacman()
    return CreateGameField(source)

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
    curr = GameCreating(settings.source)
    lb.destroy()
    c = Canvas(fr, width = settings.width - 100, height = settings.height - 100, bg = "white")
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

def ChangeSettings(arr):
    fout = open("settings.txt", "w")
    for el in arr + ["<", "0", "a", "c", ".", "fields.sv"]:
        print(el, file = fout)
    fout.close()
    menu_game()

def Error(errorlist): # To do
    app.error.delete("1.0", "end")
    for el in errorlist:
        app.error.insert("-1.0", "Incorrect form number " + str(el) + "\n")

def com():
    arr = []
    log = []
    if app.sp[0].get() in  ["3", "6", "9", "12", "15", "18", "21", "24"]:
        arr.append(app.sp[0].get())
    else:
        log.append(1)

    if app.sp[1].get() in  ["3", "6", "9", "12", "15", "18", "21", "24"]:
        arr.append(app.sp[1].get())
    else:
        log.append(2)

    try:
        if 1 <= int(app.sp[-1].get()) <= 30 :
            arr.append(app.sp[-1].get())
        else:
            log.append(6)
    except:
        log.append(6)

    try:
        if 2 <= int(app.sp[2].get()) <= 9 :
            arr.append(app.sp[2].get())
        else:
            log.append(3)
    except:
        log.append(3)

    try:    
        if 1 <= int(app.sp[3].get()) <= 9 :
            arr.append(app.sp[3].get())
        else:
            log.append(4)
    except:
        log.append(4)

    try:  
        if 1 <= int(app.sp[4].get()) <= 9 :
            arr.append(app.sp[4].get())
        else:
            log.append(5)
    except:
        log.append(5)
    
    if log != list():
        Error(sorted(log))
    else:
        ChangeSettings(arr)

def range1(a, b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr

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

    lb = Label(fr, text = "Height: ")
    lb.grid(row = 2, column = 1)
    app.add(lb)
    sc = Spinbox(fr, values = (3, 6, 9, 12, 15, 18, 21, 24))
    sc.grid(row = 2, column = 2)
    app.add_sp(sc)

    lb = Label(fr, text = "Players: ")
    lb.grid(row = 3, column = 1)
    app.add(lb)
    sc = Spinbox(fr, values = range1(2, 9))
    sc.grid(row = 3, column = 2)
    app.add_sp(sc)

    lb = Label(fr, text = "Cherry: ")
    lb.grid(row = 4, column = 1)
    app.add(lb)
    sc = Spinbox(fr, values = range1(1, 9))
    sc.grid(row = 4, column = 2)
    app.add_sp(sc)

    lb = Label(fr, text = "Apples: ")
    lb.grid(row = 5, column = 1)
    app.add(lb)
    sc = Spinbox(fr, values = range1(1, 13))
    sc.grid(row = 5, column = 2)
    app.add_sp(sc)

    lb = Label(fr, text = "Minimal distance between players: ")
    lb.grid(row = 6, column = 1)
    app.add(lb)
    sc = Spinbox(fr, values = range1(1, 30))
    sc.grid(row = 6, column = 2)
    app.add_sp(sc)

    bt = Button(fr, text = "Start Menu", command = menu_start)
    bt.grid(row = 7, column = 1)
    app.add(bt)
    bt1 = Button(fr, text = "Next", command = com)
    bt1.grid(row = 7, column = 2)
    app.add(bt1)

    text = Text(fr)
    text.grid(row = 8, column = 1, columnspan = 2)
    app.add_es(text)

def menu_credits():
    app.remove()
    f1 = Frame(root, bg = "blue", width = 600, height = 600)
    f2 = Frame(root, bg = "black")
    f3 = Frame(root, bg = "darkblue")
    f1.grid(row = 1, column = 1, columnspan = 2)
    f2.grid(row = 1, column = 3)
    f3.grid(row = 2, column = 1, columnspan = 3)
    c1 = Canvas(f1, width = 600, height = 600)
    c1.create_image(250, 300, image = logo)
    c1.pack()
    t2 = Text(f2)
    t2.insert(END, "Andrew Ishutin is a developer of this programme. \nEmail: hazmozavr@gmail.com")
    t2.pack()
    bt3 = Button(f3, text = "Back", command = menu_start)
    bt3.pack()
    app.add(f1)
    app.add(f2)
    app.add(f3)

def menu_game_from_continue(fn):
    app.remove()
    fr = Frame(bg = "black")
    fr.pack()
    lb = Label(fr, text = "Please, wait.")
    lb.pack()
    root.update()
    curr = CreateGameField(fn)
    lb.destroy()
    c = Canvas(fr, width = settings.width - 100, height = settings.height - 100, bg = "white")
    c.pack(expand=YES, fill=BOTH)   
    c.draw_gamefield(curr)
    app.add(c)
    app.add(fr)
    bt = Button(root, text = "Back", command = menu_start)
    bt.pack()
    app.add(bt)
    app.add(fr)

def menu_contunue():
    fn = filedialog.Open(filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    menu_game_from_continue(fn)

def menu_start():
    app.remove()
    fr = Frame()
    fr.pack()
    bt = Button(fr, text = "New game", command = menu_settings)
    bt.pack()
    bt2 = Button(fr, text = "Continue", command = menu_contunue)
    bt2.pack()
    app.add(bt2)
    bt3 = Button(fr, text = "Credits", command = menu_credits)
    bt3.pack()
    app.add(bt3)
    bt1 = Button(fr, text = "Quit", command = Quit)
    bt1.pack()
    app.add(fr)
    app.add(bt)
    app.add(bt1)

source = "fields.sv"
settings = prec(GetSystemMetrics(0) - 15, GetSystemMetrics(1) - 40, "3.3 beta", source) #-15, -40
root = Tk()
app = screen()
pc = PhotoImage(file = "pacman.gif") 
ap = PhotoImage(file = "apple.png") 
ch = PhotoImage(file = "cherry.png")
logo = PhotoImage(file = "KrechetBest.png")   
root.title("Pacman v" + str(settings.version))
root.geometry(str(settings.width) + 'x' + str(settings.height))
menu_start()
root.mainloop()