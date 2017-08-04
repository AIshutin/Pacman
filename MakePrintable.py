from copy import*
from tkinter import filedialog
from tkinter import *
from win32api import GetSystemMetrics
from time import*
from random import*
import subprocess

class prec:
    def __init__(self, width, height, version, source, apple):
        self.width = width
        self.height = height
        self.version = version
        self.source = source
        self.apple = apple

def _find_withtag(self, tag):
    if not self:
        return
    l = self.find_all()
    v = []
    for el in l:
        if tag in self.gettags(el):
            v.append(el)
    return tuple(v)
Canvas.find_withtag = _find_withtag

def _square(self, x, y, d, tag): #ToDo
    width = 5
    #Warning
    i, j = map(int, tag.split("x"))
    curr = "white"
    for el in teams.nm:
        if teams.cords[el] == [i, j]:
            curr = teams.col[el]
    self.create_polygon(x, y, x + d, y, x + d, y + d, x, y + d, tag = tag, fill = curr)
    self.create_line(x, y, x + d, y, width = width, tag = tag) # tag = tag
    self.create_line(x, y, x, y + d, width = width, tag = tag)    
    self.create_line(x + d, y, x + d, y + d, width = width, tag = tag)
    self.create_line(x, y + d, x + d, y + d, width= width, tag = tag)
Canvas.square = _square    

def _wall(self, x, y, d, tag):
    width = 2
    self.square(x, y, d, tag)
    a = self.create_line(x, y, x + d, y + d, width = width, tag = tag)
    b = self.create_line(x + d, y, x, y + d, width = width, tag = tag)
    c = self.create_line(x + d // 2, y, x + d / 2, y + d, width = width, tag = tag)
    d = self.create_line(x, y + d // 2, x + d, y + d // 2, width = width, tag = tag)
Canvas.wall = _wall

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
Canvas.create_circle = _create_circle

def _food(self, x, y, d, tag):
    self.square(x, y, d, tag)
    self.create_circle(x + d // 2, y + d // 2, d // 4, width = 2, tag = tag)
    #print(self.find_withtag(tag))
Canvas.food = _food

def _stuf(self, x, y, d, gif1, tag):
    self.square(x, y, d, tag)
    self.create_image(x, y, image = gif1, anchor = NW, tag= tag)
    #print(self.find_withtag(tag))
Canvas.stuf = _stuf

def _delete_withtag(self, tag):
    for el in self.find_withtag(tag):
        self.delete(el)
Canvas.delete_withtag = _delete_withtag

def replace(event):
    c = app.canv
    x, y = map(int, str(event)[str(event).find("x=") + 2:].replace("=", "").replace("y", "")[:-1].split())
    d = app.d
    j = (x - 1) // d
    i = (y - 1) // d
    app.field[i] = app.field[i][:j] + app.brash + app.field[i][j + 1:] #app.field[i][j] = app.brash()
    destroy(c)
    app.canv = Canvas(app.fr, width = settings.width - 500, height = settings.height - 100, bg = "white")
    app.canv.pack(expand=YES, fill=BOTH)   
    app.canv.draw_gamefield(app.field)
    app.canv.HotKeys("<Button-1>", replace)


def _draw_gamefield(self, curr):   
    h = len(curr)
    w = len(curr[0])
    w_r = (settings.width - 500) // w
    h_r = (settings.height - 100)// h
    d = min(w_r, h_r)
    app.d = d
    for i in range(h):
        for j in range(w):
            x = j * d
            y = i * d
            if (h > w):
                x, y = y, x
            if curr[i][j] == "0":
                self.wall(x, y, d, str(i) + "x" + str(j))
            if curr[i][j] == ".":
                self.food(x, y, d, str(i) + "x" + str(j))
            if curr[i][j] == "<":
                self.stuf(x, y, d, pc, str(i) + "x" + str(j))
            if curr[i][j] == "a":
                self.stuf(x, y, d, ap, str(i) + "x" + str(j))
            if curr[i][j] == "c":
                self.stuf(x, y, d, ch, str(i) + "x" + str(j))
            if curr[i][j] == "e": #empty
                self.square(x, y, d, str(i) + "x" + str(j))
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
            app.field = curr
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
        obj.pack_forget()
    except:
        pass
    try:
        obj.grid_forget()
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
        self.canv = []
        self.field = [[]]
        self.brash = "0"
        self.d = 0
        self.killed = []
        self.fr = []
        self.f = []

    def change_field(self, curr):
        self.field = deepcopy(curr)

    def change_brash(self, s):
        self.brash = s

    def add(self, arg):
        self.window.append(arg)
    
    def add_sp(self, arg):
        self.add(arg)
        self.sp.append(arg)
    
    def add_es(self, arg):
        self.add(arg)
        self.error = arg

    def add_ca(self, arg):
        self.add(arg)
        self.canv = arg

    def add_fr_of_ca(self, arg):
        self.add(arg)
        self.fr = arg

    def add_score(self, arg):
        self.add(arg)
        self.score = arg

    def remove(self):
        for el in self.window:
            destroy(el)
        self.window = []
        self.sp = []
        self.error = []
        self.canv = []
        self.f = []

def Brush_wall():
    app.change_brash("0")

def Brush_pacman():
    app.change_brash("<")

def Brush_cherry():
    app.change_brash("c")

def Brush_apple():
    app.change_brash("a")

def Brush_food():
    app.change_brash(".")

def _tag_blind_withtag(self, tag, event, func):
    for el in self.find_withtag(tag):
        self.tag_bind(el, event, func)
Canvas.tag_blind_withtag = _tag_blind_withtag

def goto_menu_map_new():
    app.remove()
    lb = Label(text = "Please, wait.")
    lb.pack()
    app.add(lb)
    GameCreating(settings.source)
    lb.destroy()
    menu_map()

def save_file():
    fout_name = filedialog.SaveAs(root, filetypes = [('*.txt files', '.txt')]).show()
    if not fout_name:
        return
    fout = open(fout_name, "w")
    for el in app.field:
        print(el, file = fout)
    fout.close()

def _HotKeys(self, key, func):
    h = len(app.field)
    w = len(app.field[0])
    for i in range(len(app.field)):
        for j in range(len(app.field[0])):
            if h > w:
                i, j = j, i
            self.tag_blind_withtag(str(i) + "x" + str(j), key, func)
Canvas.HotKeys = _HotKeys

def menu_map():
    app.remove()
    fr = Frame(bg = "black")
    fr.pack(padx = 10, pady = 10)
    root.update()
    c = Canvas(fr, width = settings.width - 100, height = settings.height - 100, bg = "white")
    c.pack(expand=YES, fill=BOTH)   
    c.draw_gamefield(app.field)
    app.add_ca(c)
    app.add_fr_of_ca(fr)
    fr2 = Frame()
    fr2.pack()
    app.add(fr2)
    bt = Button(fr2, text = "Back", command = menu_settings)
    bt.grid(row = 1, column = 1)
    bt2 = Button(fr2, text = "Wall", command = Brush_wall)
    bt2.grid(row = 1, column = 2)
    bt3 = Button(fr2, text = "Food", command = Brush_food)
    bt3.grid(row = 1, column = 3)
    app.add(bt3)
    bt4 = Button(fr2, text = "Pacman", command = Brush_pacman)
    bt4.grid(row = 1, column = 4)
    app.add(bt4)
    bt5 = Button(fr2, text = "Apple", command = Brush_apple)
    bt5.grid(row = 1, column = 5)
    app.add(bt4)   
    bt6 = Button(fr2, text = "Cherry", command = Brush_cherry)
    bt6.grid(row = 1, column = 6)
    app.add(bt6)       
    c.HotKeys("<Button-1>", replace)
    app.add(bt2)
    app.add(bt)
    app.add(fr)
    bt7 = Button(fr2, text = "Next", command = menu_teams)
    bt7.grid(row = 1, column = 7)
    app.add(bt7)

    bt8 = Button(fr2, text = "Load", command = menu_continue_map)
    bt8.grid(row = 1, column = 8)
    app.add(bt8)

    bt9 = Button(fr2, text = "Save", command = save_file)
    bt9.grid(row = 1, column = 9)
    app.add(bt9)


def Quit():
    cmd = 'cleaner.bat'
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True) #stderr=subprocess.STDOUT
    exit(0)

def ChangeSettings(arr):
    fout = open("settings.txt", "w")
    for el in arr + ["<", "0", "a", "c", ".", "fields.sv"]:
        print(el, file = fout)
    fout.close()
    goto_menu_map_new()

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

def menu_map_continue(fn):
    CreateGameField(fn)
    menu_map()

def menu_continue_map():
    fn = filedialog.Open(filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    menu_map_continue(fn)

class team_data():
    colors = ["white", "grey", "green", "blue", "darkblue", "yellow", "orange", "pink", "purple"]

    def __init__(self):
        self.nm = []
        self.score = dict()
        self.curr = dict()
        self.apple = dict()
        self.col = dict()
        self.cords = dict()
        self.logs = dict()
        #self.avcol = list(self.colors)
    
    def add_team(self, s, score, col):
        self.nm.append(s)
        self.score[s] = score
        self.apple[s] = 0
        self.curr[s] = 0
        #i = randint(0, len(self.avcol) - 1)
        self.col[s] = col
        self.logs[s] = False
        #self.avcol.pop(i)


    def add_points(self, team, n):
        self.curr[team] += n

    def add_apple_points(self, team):
        self.apple[team] += settings.apple

    def end(self):
        ans = []
        for el in self.nm:
            self.score[el] += self.apple[el] + self.curr[el]
            ans.append([el, self.score[el]])
        return ans

    def kill(self, killer, food):
        self.curr[killer] += self.curr[food]
        self.curr[food] = 0

    def reset(self):
        self.nm = []
        self.score = dict()
        self.curr = dict()
        self.apple = dict()  
        self.col = dict()
        self.cords = dict()
        self.logs = dict()
        #self.avcol = list(self.colors)

class score_table(): #Bad but working, I hope.
    
    def __init__(self, root, n):
        self.fr = Frame(root)
        self.t = []
        self.s = []
        self.n = n
        for i in range(self.n):
            en = Entry(self.fr, bg = teams.col[teams.nm[i]])
            en.insert(0, teams.nm[i])
            self.t.append(en)
            sc = Entry(self.fr, bg = teams.col[teams.nm[i]])
            sc.insert(0, teams.curr[teams.nm[i]])
            self.s.append(sc)
    
    def pack(self):
        self.fr.pack()
        app.add(self.fr)
        for i in range(self.n):
            self.t[i].grid(row = i, column = 1, columnspan = 2)
            self.s[i].grid(row = i, column = 3, columnspan = 1)
            app.add(self.t[i])
            app.add(self.s[i])

    def update(self):
        for i in range(self.n):
            self.s[i].delete(0, END)
            self.s[i].insert(0, teams.curr[teams.nm[i]] + teams.apple[teams.nm[i]])

    def destroy(self):
        for i in range(self.n):
            self.t[i].destroy()
            self.s[i].destroy()
        self.fr.destroy()

def update_score():
    app.score.update()

def allow(cord1, cord2): #ToDo
    global END_GAME
    if END_GAME == 1:
        return False
    if app.field[cord2[0]][cord2[1]] == "0":
        return False
    if cord1 == []:
        return False
    if app.field[cord1[0]][cord1[1]] != "<":
        return False
    if (abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1]) > 1):
        return False
    st = -1
    en = -1
    for el in teams.nm:
        if teams.cords[el] == cord1:
            st = el
        elif teams.cords[el] == cord2:
            en = el
    if en != -1:
        if not teams.logs[st]:
            return False
        teams.kill(st, en)
        teams.cords[en] = [-1, -1]
        END_GAME = 1 #End of the game
    else:
        if app.field[cord2[0]][cord2[1]] == "a":
            teams.add_apple_points(st)
        if app.field[cord2[0]][cord2[1]] == "c":
            teams.logs[st] = True
        if app.field[cord2[0]][cord2[1]] == ".":
            teams.add_points(st, 1)
    teams.cords[st] = cord2
    app.score.update()
    return True

def replace2(event):
    if app.f == []:
        return
    c = app.canv
    x, y = map(int, str(event)[str(event).find("x=") + 2:].replace("=", "").replace("y", "")[:-1].split())
    d = app.d
    j = (x - 1) // d
    i = (y - 1) // d
    if allow(app.f, [i, j]):
        app.brash = "<"
        i = app.f[0]
        j = app.f[1]
        app.field[i] = app.field[i][:j] + "e" + app.field[i][j + 1:]
        replace(event)
    app.canv.HotKeys("<Button-1>", replace2)
    app.canv.HotKeys("<Button-3>", replace3)

def replace3(event):
    c = app.canv
    x, y = map(int, str(event)[str(event).find("x=") + 2:].replace("=", "").replace("y", "")[:-1].split())
    d = app.d
    j = (x - 1) // d
    i = (y - 1) // d
    app.f = [i, j]

def menu_game(): #ToDo
    app.remove()
    fr = Frame(bg = "black")
    fr.grid(row = 1, column = 1, columnspan = 4)
    c = Canvas(fr, width = settings.width - 500, height = settings.height - 100, bg = "white")
    c.pack(expand=YES, fill=BOTH)
    c.draw_gamefield(app.field)
    app.add_fr_of_ca(fr)
    app.add_ca(c)
    fr2 = Frame()
    fr3 = Frame()
    fr2.grid(row = 1, column = 5, columnspan = 1)
    fr3.grid(row = 2, column = 1, columnspan = 5)
    app.add(fr2)
    app.add(fr3)
    bt1 = Button(fr3, text = "Back", command = menu_teams)
    bt2 = Button(fr3, text = "Quit", command = menu_start)
    bt1.grid(row = 1, column = 1)
    bt2.grid(row = 1, column = 3)
    app.add(bt1)
    app.add(bt2)
    n = 0 # number of teams
    for el in app.field:
        n += el.count("<")
    # n is calculated
    st = score_table(fr2, n)
    fr5 = Frame(fr2)
    st.pack()
    fr5.pack()
    app.add_score(st)
    app.add(fr5)
    app.change_brash("<")
    print("EEE")
    c.HotKeys("<Button-1>", replace2)
    c.HotKeys("<Button-3>", replace3)


def PrepareForGame():
    n = 0 # number of teams
    for el in app.field:
        n += el.count("<")
    # n is calculated

    t = [] #list of names of teams
    sc = [] #list of scores of teams
    state = 0 # 0 = Name of team, 1 = Score of team
    log = [] # All data is valide
    prev = set() # set of names of teams
    cnt = 0
    for el in app.sp:
        if state == 1:
            try:
                sc.append(int(el.get())) 
            except:
                log.append(cnt + 1) #We have found an error. el.get() is not an int
        else:
            if el.get() in prev:
                log.append(cnt + 1)
            prev.add(el.get())
            t.append(el.get())
        cnt += state
        state = (state + 1) % 2
    if log != []:
        Error(log)
        return
    for i in range(n):
        teams.add_team(t[i], sc[i], teams.colors[i])
    cords = []
    prev = 0
    for i in range(len(app.field)):
        for j in range(len(app.field[0])):
            if app.field[i][j] == "<":
                teams.cords[t[prev]] = [i, j]
                prev += 1
    menu_game()

def Void():
    pass

def menu_teams():
    app.remove()
    n = 0
    for el in app.field:
        n += el.count("<")
    lb1 = Entry()
    lb2 = Entry()
    lb1.insert(0, "Teams")
    lb2.insert(0, "Score")
    app.add(lb1)
    app.add(lb2)
    lb1.grid(row = 1, column = 1, columnspan = 2)
    lb2.grid(row = 1, column = 3)
    for i in range(n):
        lb1 = Entry(bg = teams.colors[i])
        lb1.insert(0, "Name of team №" + str(i))
        lb1.grid(row = i + 2, column = 1, columnspan = 2)
        app.add_sp(lb1)
        lb1 = Entry(bg = teams.colors[i])
        lb1.insert(0, "0")
        lb1.grid(row = i + 2, column = 3)
        app.add_sp(lb1) 
    bt = Button(text = "Back", command = menu_map)
    bt.grid(row = n + 3, column = 1)
    app.add(bt)
    bt2 = Button(text = "Next", command = PrepareForGame)
    bt2.grid(row = n + 3, column = 3)
    app.add(bt2)
    text = Text()
    text.grid(row = n + 4, column = 3)
    app.add_es(text)

def menu_start():
    app.remove()
    fr = Frame()
    fr.pack()
    bt = Button(fr, text = "New game", command = menu_settings)
    bt.pack()
    bt2 = Button(fr, text = "Continue")
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

teams = team_data()
source = "fields.sv"
settings = prec(GetSystemMetrics(0) - 15, GetSystemMetrics(1) - 40, "3.4 beta", source, 5) #-15, -40
root = Tk()
app = screen()
pc = PhotoImage(file = "pacman.gif") 
ap = PhotoImage(file = "apple.png") 
ch = PhotoImage(file = "cherry.png")
logo = PhotoImage(file = "KrechetBest.png")   
root.title("Pacman v" + str(settings.version))
root.geometry(str(settings.width) + 'x' + str(settings.height))
END_GAME = 0 #not const but flag
menu_start()
root.mainloop()