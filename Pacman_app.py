from copy import*
from tkinter import filedialog
import tkinter.font as font
import tkinter
from win32api import GetSystemMetrics #For screen resolution
from time import*
from random import*
import subprocess #For Batch scripts

'''
AIs Software
Information for moders.
This is my first so big program, that`s why it`s so strange and wierd.
Don`t try to read it from begin to end.
Read it like dfs || bfs, start of logic is in the end of the code.
Also it`s my first documentation, so lucky you are!
But you almost have one hope: my email: hazmozavr@gmail.com or
ask Elena Borisvna to tell you my contact.

I also have some information to tell you which
explains why my code is these code.

I afraid my Pacman.exe
I forgot how I made that
And my c++ compiler and random module are broken at this moment.

Some functions in tkinter aren`t working at this moment. So, I remade them

My "N" key is broken. So sometimes it`s possible that I will miss "n" in words.
'''

#Remaking Tkinter methods
def _find_withtag(self, tag): #The same as in tkinter but working
    if not self:
        return
    l = self.find_all()
    v = []
    for el in l:
        if tag in self.gettags(el):
            v.append(el)
    return tuple(v)
tkinter.Canvas.find_withtag = _find_withtag

def _delete_withtag(self, tag): #The same as in tkinter but working
    for el in self.find_withtag(tag):
        self.delete(el)
tkinter.Canvas.delete_withtag = _delete_withtag

def _tag_blind_withtag(self, tag, event, func):
    for el in self.find_withtag(tag):
        self.tag_bind(el, event, func)
tkinter.Canvas.tag_blind_withtag = _tag_blind_withtag

#Adding new methods
def _square(self, x, y, d, tag): #Special method to draw square
    # d - is size of board of square
    width = 5
    #Warning
    i, j = map(int, tag.split("x"))
    curr = "white"
    for el in teams.nm:
        if teams.cords[el] == [i, j]:
            curr = teams.col[el]
    self.create_polygon(x, y, x + d, y, x + d, y + d, x, y + d, tag = tag, fill = curr) 
    # ^For comfortable clicking on ceils^
    self.create_line(x, y, x + d, y, width = width, tag = tag) # tag = tag
    self.create_line(x, y, x, y + d, width = width, tag = tag)    
    self.create_line(x + d, y, x + d, y + d, width = width, tag = tag)
    self.create_line(x, y + d, x + d, y + d, width= width, tag = tag)
tkinter.Canvas.square = _square    

def _wall(self, x, y, d, tag): #Special method to draw wall. Feel free to change.
    width = 2
    self.square(x, y, d, tag)
    a = self.create_line(x, y, x + d, y + d, width = width, tag = tag)
    b = self.create_line(x + d, y, x, y + d, width = width, tag = tag)
    c = self.create_line(x + d // 2, y, x + d / 2, y + d, width = width, tag = tag)
    d = self.create_line(x, y + d // 2, x + d, y + d // 2, width = width, tag = tag)
tkinter.Canvas.wall = _wall

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
tkinter.Canvas.create_circle = _create_circle

def _food(self, x, y, d, tag):
    self.square(x, y, d, tag)
    self.create_circle(x + d // 2, y + d // 2, d // 4, width = 2, tag = tag)
tkinter.Canvas.food = _food

def _stuf(self, x, y, d, gif1, tag):
    self.square(x, y, d, tag)
    self.create_image(x, y, image = gif1, anchor = NW, tag= tag)
tkinter.Canvas.stuf = _stuf

def _draw_gamefield(self, curr): 
    app.used = set()  
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
tkinter.Canvas.draw_gamefield = _draw_gamefield

def _normalize(self): # Make Canvas normal size
    z = self.bbox(ALL)
    a, b, c, d = z[0], z[1], z[2], z[3]
    self.config(height = abs(b - d), width = abs(a - c))
tkinter.Canvas.normalize = _normalize

def _HotKeys(self, key, func):
    h = len(app.field)
    w = len(app.field[0])
    for i in range(len(app.field)):
        for j in range(len(app.field[0])):
            self.tag_blind_withtag(str(i) + "x" + str(j), key, func)
tkinter.Canvas.HotKeys = _HotKeys

tkinter.Entry._insert1 = tkinter.Entry.insert
def _insert(self, n, text):
    self._insert1(n, lang.translate(text))
tkinter.Entry.insert = _insert

#Shortcuts&more
def Button(root = None, **keyargs): # Function for fast creating buttons with custom parametres for fast modifing
    z = tkinter.Button(root, **keyargs)
    app.add(z)
    z.config(text = lang.translate(z.config()["text"][-1]))
    return z

def Canvas(root = None, **keyargs): # Function for fast creating canvases with custom parametres for fast modifing
    z = tkinter.Canvas(root, **keyargs)
    app.add(z)
    return z

def Frame(root = None, **keyargs): # Function for fast creating frames with custom parametres for fast modifing
    z = tkinter.Frame(root, **keyargs)
    app.add(z)
    return z

def Label(root = None, **keyargs):
    z = tkinter.Label(root, **keyargs)
    app.add(z)
    z.config(text = lang.translate(z.config()["text"][-1]))
    return z

def Message(root = None, **keyargs):
    text = ""
    for el in keyargs:
        #print(el)
        if el == "text":
            print(keyargs)

            text = keyargs[el]
    z = tkinter.Message(root, **keyargs)
    if text != "":
        z.config(text = lang.translate(text))
    else:
        z.config(text = "")
    app.add(z)
    return z

#Creating classes
class prec: 
    def __init__(self, width, height, version, source, apple):
        self.width = width
        self.height = height
        self.version = version
        self.source = source
        self.apple = apple
        self.n = 0

class screen: #Represents what is on the screen and allows commands outside menu use vidgets of menu
    """docstring for  screen"""
    def __init__(self):
        self.window = []
        self.sp = []
        self.error = []
        self.canv = []
        self.field = [[]]
        self.brash = "0"
        self.d = 0
        self.fr = []
        self.f = []
        self.used = set()

    def change_field(self, curr):
        self.field = deepcopy(curr)

    def change_brash(self, s):
        self.brash = s

    def add(self, arg):
        self.window.append(arg)
    
    def add_sp(self, arg): #Add Spinbox
        self.add(arg)
        self.sp.append(arg)
    
    def add_es(self, arg): #Add text for error messages
        self.add(arg)
        self.error = arg

    def add_ca(self, arg): #Add canvas
        self.add(arg)
        self.canv = arg

    def add_fr_of_ca(self, arg): #Add parent frame of canvas
        self.add(arg)
        self.fr = arg

    def add_score(self, arg): #Add score table vidget
        self.add(arg)
        self.score = arg

    def remove(self): #Function to clear screen
        for el in self.window:
            destroy(el)
        self.window = []
        self.sp = []
        self.error = []
        self.canv = []
        self.f = []
        self.used = set()

class ad_vid: #Not for moding, please. #A vidget for my ad
    
    def __init__(self, root, **keyargs):
        self.fr = Frame(root, **keyargs)
        self.canv = Canvas(self.fr)
        self.text = tkinter.Message(self.fr, text = "AI`s Software\n", width = 2002)

    def pack(self, **keyargs):
        self.fr.pack(**keyargs)
        self.canv.pack()
        self.canv.create_image(0, 0, image = theme, anchor = "nw")
        self.canv.normalize()
        self.text.pack()

    def destroy(self):
        destroy(self.fr)

class team_data(): #Class for storing and updating information about teams. Like database.
    colors = ["grey", "green", "salmon1", "cyan", "yellow", "orange", "light sky blue", "MistyRose3", "khaki"]

    def __init__(self):
        self.nm = []
        self.score = dict()
        self.curr = dict()
        self.apple = dict()
        self.col = dict()
        self.cords = dict()
        self.logs = dict()
        self.shields = dict()
        self.hist = dict()
    
    def add_team(self, s, score, col):
        self.nm.append(s)
        self.score[s] = score
        self.apple[s] = 0
        self.curr[s] = 0
        self.col[s] = col
        self.logs[s] = False
        self.cords [s] = []
        self.shields[s] = 0
        self.hist[s] = [[-1, -1]]

    def add_points(self, team, n):
        self.curr[team] += n

    def add_apple_points(self, team):
        self.apple[team] += settings.apple

    def kill(self, killer, food):
        self.curr[killer] += self.curr[food]
        self.curr[food] = 0
        self.shields[food] = 1

    def reset(self):
        self.nm = []
        self.score = dict()
        self.curr = dict()
        self.apple = dict()  
        self.col = dict()
        self.cords = dict()
        self.logs = dict()
        self.shields = dict()
        self.hist = dict()

class hist: #Class for storing history of movings of pacmans
    
    def __init__(self):
        self.changes = []   
    
    def add(self, z):
        self.changes.append(z)
    
    def last(self): #Gives last change and update it
        if len(self.changes) < 1:
            return False
        q = self.changes[-1]
        self.changes.pop(-1)
        return q

class param: #Speccial class for some parametres. 
    
    def __init__(self, END_GAME, SHIELD, SPACE_STRING):
        self.END_GAME = END_GAME #not const but flag. Sorry for style. 1 - game is ended, 0 it`s not
        self.SHIELD = SHIELD #not const but flag. 0 - Shields don`t exist in the game. 1 - it do
        self.SPACES = SPACE_STRING # This is constant value. 

class score_table(): #Special class for making and updating score tables 
    
    def __init__(self, root):
        self.fr = Frame(root)
        self.t = []
        self.s = []
        self.n = settings.n
        for i in range(self.n):
            en = tkinter.Entry(self.fr, bg = teams.col[teams.nm[i]], font = MyFont)
            en.insert(0, teams.nm[i])
            self.t.append(en)
            sc = tkinter.Entry(self.fr, bg = teams.col[teams.nm[i]], font = MyFont)
            sc.insert(0, teams.curr[teams.nm[i]] + teams.apple[teams.nm[i]])
            self.s.append(sc)
    
    def pack(self): #Defining pack method
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

class language: #module for translating
    lang = {"English": 1, "Русский": 0} #list of avaliable languages
    lang_list = ["Русский", "English"] # real list

    def __init__(self):
        self.ru = { # English to Russian dictionary
            "Load": "Загрузить",
            "Save": "Сохранить",
            "Next": "Далее",
            "Back": "Назад",
            "Continue": "Продолжить",
            "New game": "Новая игра",
            "Credits": "Об авторе",
            "Quit": "Выход",
            "Wall": "Стена",
            "Apple": "Яблоко",
            "Cherry": "Вишенка",
            "Pacman": "Пэкмэн",
            "Food": "Пища",
            "Return": "Обратно",
            "New round": "Новый раунд",
            "Width:": "Ширина:",
            "Height:": "Высота:",
            "Cherry:": "Вишенки:",
            "Apples:": "Яблоки:",
            "Minimal distance:": "Минимальное расстояние:",
            "Please, wait...": "Пожалуйста, подождите",
            "Teams": "Команда",
            "Score": "Фора",
            "Do shields exists:": "Есть ли в игре щиты:",
            "Number of teams:": "Кол-во команд:",
            "Cost of an apple:": "Цена яблока",
            "End game": "Закончить игру",
            "Yes": "Да",
            "No": "Нет",
            "Empty map": "Пустая карта",
            "The distance between players is too big for this gamefield.": "Расстояние между игроками слишком большое для этого поля.",
            "Too many objects for this gamefield.": "Слишком объектов для этого поля.",
            "Incorrect form number": "Неправильная форма №",
            "About": "Об авторе"
        }
        self.curr = 0 # 1 - English, 0 - Russian . Defines current language mod
    
    def change(self, str1): # Changes language
        if str1 not in self.lang:
            return False
        self.curr = self.lang[str1]
        return True

    def translate(self, str1): # Translates phrase or word to current language 
        if self.curr == 0: # Russian
            i = 0
            str1 = str(str1)
            while str1[i] == " ":
                i += 1
            j = len(str1) - 1
            cnt = 0
            while str1[j] == " ":
                j -= 1
                cnt += 1
            str1 = str1[i:j + 1]
            z = ""
            if str1 not in self.ru:
                #print(str1) #ToDo
                return " " * i + str1 + z + " " * cnt 
            return " " * i + self.ru[str1] + z + " " * cnt
        else: # English
            return str1

def save_game():
    fn = filedialog.SaveAs(root, filetypes = [('*.game files', '.game')]).show()
    if not fn:
        return
    fout = open(fn, "w")
    print(len(teams.nm), file = fout)
    for el in teams.nm:
        print(len(list(el.split())), el, teams.curr[el], teams.col[el], teams.shields[el], file = fout)
    fout.close()

def load_game():
    teams.reset()
    parametres.END_GAME = 0
    fn = filedialog.Open(root, filetypes = [('*.game files', '.game')]).show()
    if not fn:
        return
    fin = open(fn)
    try:
        z = fin.readline().rstrip()
        settings.n = int(z)
        for i in range(settings.n):
            z = list(fin.readline().rstrip().split())
            n = int(z[0])
            name = z[1]
            for i in range(2, 1 + n):
                name = name + " " + z[i]
            score = z[n + 1]
            col = z[n + 2]
            teams.add_team(name, int(score), col)
            teams.shields[name] = int(z[n + 3])
        font.nametofont('TkDefaultFont').configure(size=20) #ToDo
        menu_settings()
    except:
        return

def save_file(): #Save map
    fout_name = filedialog.SaveAs(root, filetypes = [('*.map files', '.map')]).show()
    if not fout_name:
        return
    fout = open(fout_name, "w")
    for el in app.field:
        print(el, file = fout)
    fout.close()

def replace(event): #Changes some ceil.
    c = app.canv
    x, y = map(int, str(event)[str(event).find("x=") + 2:].replace("=", "").replace("y", "")[:-1].split())
    d = app.d
    j = (x - 1) // d
    i = (y - 1) // d
    app.field[i] = app.field[i][:j] + app.brash + app.field[i][j + 1:] #app.field[i][j] = app.brash()
    
    c.delete_withtag(str(i) + "x" + str(j))
    x = j * d
    y = i * d
    if app.field[i][j] == "0":
        c.wall(x, y, d, str(i) + "x" + str(j))
    if app.field[i][j] == ".":
        c.food(x, y, d, str(i) + "x" + str(j))
    if app.field[i][j] == "<":
        c.stuf(x, y, d, pc, str(i) + "x" + str(j))
    if app.field[i][j] == "a":
        c.stuf(x, y, d, ap, str(i) + "x" + str(j))
    if app.field[i][j] == "c":
        c.stuf(x, y, d, ch, str(i) + "x" + str(j))
    if app.field[i][j] == "e": #empty
        c.square(x, y, d, str(i) + "x" + str(j))
    app.canv.tag_blind_withtag(str(i) + "x" + str(j), "<Button-1>", replace)

def CPacman(): #Function for working with C++ Pacman.exe with Batch commands
    cmd = 'helper.bat'
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
    z = clock()
    while clock() - z < 2:
        root.update()
    while True:
        try:
            root.update()
            z = open("sys")
            if z.readline().rstrip() == '1':
                z.close()
                break
            z.close()
        except:
            sleep(1)
            break

def CreateGameField(source): #Function for reading gamefield from file
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

def destroy(obj): #Function for normal deleting any object. Even frames. Even grided frames.
    if (not obj):
        return
    try:
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

def Quit(): #Quit with killing 3 working pacman.exe
    cmd = 'cleaner.bat'
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True)
    exit(0)

def ChangeSettings(arr): #Function for writing in file for communicating with pacman.exe 
    fout = open("settings.txt", "w")
    for el in arr + ["<", "0", "a", "c", ".", "fields.sv"]:
        print(el, file = fout)
    fout.close()
    goto_menu_map_new()

def Error(errorlist): #Simple function to warn user about not valide input
    for i in range(len(errorlist)):
        errorlist[i] = str(errorlist[i])
    app.error.config(text = "\n".join(errorlist))
    '''
    app.error.delete("1.0", "end")
    for el in errorlist:
        app.error.insert("-1.0", lang.translate("Incorrect form number ") + str(el) + "\n")'''

def com(): #Function that read information from setting menu
    global app
    arr = [] #Good information from user
    log = [] #User`s mistakes
    spec1 = False #Special error number 1
    spec2 = False #Special error number 2
    #Width
    s = "Incorrect form number "
    if app.sp[0].get() in  ["3", "6", "9", "12", "15", "18", "21", "24"]:
        arr.append(int(app.sp[0].get()))
    else:
        log.append(1)

    #Height
    if app.sp[1].get() in  ["3", "6", "9", "12", "15", "18", "21", "24"]:
        arr.append(int(app.sp[1].get()))
    else:
        log.append(2)

    #Minimal distance between player and player
    try:
        if 1 <= int(app.sp[-1].get()) <= 30:
            arr.append(int(app.sp[-1].get()))
            if ((arr[0] - 1) // arr[2] + 1) * ((arr[1] - 1) // arr[2] + 1) < settings.n:
                spec1 = True
        else:
            log.append(5)
    except:
        log.append(5)

    #Adding number of players
    arr.append(settings.n)

    #Cherry
    try:    
        if 0 <= int(app.sp[2].get()) <= 9 :
            arr.append(int(app.sp[2].get()))
        else:
            log.append(3)
    except:
        log.append(3)

    #Apple
    try:  
        if 0 <= int(app.sp[3].get()) <= 9 :
            arr.append(int(app.sp[3].get()))
        else:
            log.append(4)
    except:
        log.append(4)
    try:
        if arr[-1] + arr[-2] + arr[-3] > arr[0] * arr[1]:
            spec2 = True
    except:
        pass

    #Option for creating map only by user
    if int(app.cb_var.get()) == 1 and "1" not in log and "2" not in log:
        if arr[1] > arr[0]: # Turning gamefield 
            arr[0], arr[1] = arr[1], arr[0]
        app.field = ["0" * int(arr[0]) for i in range(int(arr[1]))]
        menu_map()
        return

    if log != list() or spec1 or spec2: #There are some mistakes
        es = []
        for el in sorted(log):
            es.append(lang.translate(s) + str(el))
        if spec1:
            es.append(lang.translate("The distance between players is too big for this gamefield."))
        if spec2:
            es.append("-1.0", lang.translate("Too many objects for this gamefield."))
        Error(sorted(es))
        
    else:   
        if arr[1] > arr[0]: # Turning gamefield 
            arr[0], arr[1] = arr[1], arr[0]
        ChangeSettings(arr)

def range1(a, b): #Simple function to make list of range from a to b
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr

def menu_map_continue(fn):
    CreateGameField(fn)
    menu_map()

def menu_continue_map():
    fn = filedialog.Open(filetypes = [('*.map files', '.map')]).show()
    if fn == '':
        return
    menu_map_continue(fn)

def allow(cord1, cord2): #Fuction that determinate is action valide or not
    
    if parametres.END_GAME == 1: #The game is ended
        return False

    if app.field[cord2[0]][cord2[1]] == "0": #If we want to move on ceil with wall
        return False

    if cord1 == []: #If we don`t know our starting position
        return False

    if app.field[cord1[0]][cord1[1]] != "<": #If we move not pacman
        return False

    if (abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1]) > 1): #If we are trying to jump
        return False

    st = -1 #Starting pacman id
    en = -1 #Prey pacman id if exists
    if cord1 == cord2: #If we are not going to move to another ceil
        return False

    for el in teams.nm: # Searching ids
        if teams.cords[el] == cord1:
            st = el
        elif teams.cords[el] == cord2:
            en = el

    if en != -1: #We are going to eat someone
        if not teams.logs[st]: #cherry factor
            return False
        if parametres.SHIELD == 1 and teams.shields[en] == 1: #Maybe he has a shield
            return False
        archive.add([deepcopy(teams), deepcopy(app.field), deepcopy(parametres)]) #Saving previous state
        for el in teams.nm:
            teams.shields[el] = 0 #Because game is ended
        teams.kill(st, en)
        teams.cords[en] = [-1, -1] 
        parametres.END_GAME = 1 #End of the game
    else:
        archive.add([deepcopy(teams), deepcopy(app.field), deepcopy(parametres)])
        if app.field[cord2[0]][cord2[1]] == "a": #eating apple
            teams.add_apple_points(st)
        if app.field[cord2[0]][cord2[1]] == "c": #eating cherry
            teams.logs[st] = True
        if app.field[cord2[0]][cord2[1]] == ".": #eating food
            teams.add_points(st, 1)
    teams.cords[st] = cord2
    app.score.update()
    teams.hist[st].append(cord1)
    return True

def replace2(event): #function that moves pacmans in the game
    if app.f == []:
        return
    c = app.canv
    #Calculating position of the object
    x, y = map(int, str(event)[str(event).find("x=") + 2:].replace("=", "").replace("y", "")[:-1].split())
    d = app.d
    j = (x - 1) // d
    i = (y - 1) // d

    if allow(app.f, [i, j]): #Changing gamefield
        i = app.f[0]
        j = app.f[1]
        app.field[i] = app.field[i][:j] + "e" + app.field[i][j + 1:]
        app.canv.delete_withtag(str(i) + "x" + str(j))
        app.canv.square(app.f[1] * d, app.f[0] * d, d, str(i) + "x" + str(j))
        app.canv.tag_blind_withtag(str(i) + "x" + str(j), "<Button-3>", replace3)
        app.canv.tag_blind_withtag(str(i) + "x" + str(j), "<Button-1>", replace2)
        app.brash = "<"
        replace(event)
        j = (x - 1) // d
        i = (y - 1) // d
        app.canv.tag_blind_withtag(str(i) + "x" + str(j), "<Button-1>", replace2)
        app.canv.tag_blind_withtag(str(i) + "x" + str(j), "<Button-3>", replace3)

def replace3(event): #Saving our starting location
    c = app.canv
    x, y = map(int, str(event)[str(event).find("x=") + 2:].replace("=", "").replace("y", "")[:-1].split())
    d = app.d
    j = (x - 1) // d
    i = (y - 1) // d
    app.f = [i, j]

def prev_change(): #Function that allows to return to earlier state
    global teams, app, parametres
    z = archive.last()
    if z == False:
        return False
    teams = deepcopy(z[0])
    app.field = deepcopy(z[1])
    parametres = deepcopy(z[2])
    app.canv.draw_gamefield(app.field)
    app.score.update()
    app.canv.HotKeys("<Button-1>", replace2)
    app.canv.HotKeys("<Button-3>", replace3)
    return True

def another_language():
    bt = app.lang_bt
    curr = lang.lang_list[(lang.curr + 1) % len(lang.lang)]
    bt.config(text = curr)
    lang.change(curr)
    menu_start()

def PrepareForGame(): #Function that adds teams from team menu
    n = settings.n
    t = [] #list of names of teams
    sc = [] #list of scores of teams
    state = 0 # 0 = Name of team, 1 = Score of team
    log = [] # All data is valide
    prev = set() # set of names of teams
    cnt = 0
    s = "Incorrect form number "
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
        es = []
        for el in log:
            es.append(lang.translate(s) + str(el))
        Error(es)
        return
    for i in range(n):
        teams.add_team(t[i], sc[i], teams.colors[i])
    menu_settings()

def new_game(): #Function that sets all values to special state to play again and save current achievments
    global archive
    parametres.END_GAME = 0
    for el in teams.nm:
        teams.score[el] += teams.curr[el] + teams.apple[el]
        teams.curr[el] = teams.apple[el] = 0
        teams.cords[el] = []
        teams.hist[el] = [[-1, -1]]
    archive = hist()
    menu_settings()

def goto_menu_map_new():
    app.remove()
    lb = Label(text = "Please, wait...")
    lb.pack()
    app.add(lb)
    GameCreating(settings.source)
    lb.destroy()
    menu_map()

def goto_menu_game():
    n = 0
    for el in app.field:
        n += el.count('<')
    if n != settings.n:
        return
    #Error message
    DefineTeamsLocation()
    menu_game()

def DefineTeamsLocation(): #Function that associate team with ceil on gamefield
    prev = 0
    t = []
    for el in teams.nm:
        t.append(el)
    for i in range(len(app.field)):
        for j in range(len(app.field[0])):
            if app.field[i][j] == "<":
                teams.cords[t[prev]] = [i, j]
                prev += 1

def goto_menu_teams():
    log = []
    s = "Incorrect form number "
    try:
        if 2 <= int(app.sp[0].get()) <= 9 :
            settings.n = int(app.sp[0].get())
        else:
            log = [1]
    except:
        log = [1]
    
    try:
        settings.apple = int(app.sp[1].get())
    except:
        log.append(2)

    if app.sp[2].get() == lang.translate("Yes"):
        parametres.SHIELD = 0
    elif app.sp[2].get() == lang.translate("No"):
        parametres.SHIELD = 1
    else:
        log.append(3)

    if log != []:
        es = []
        for el in log:
            es.append(lang.translate(s) + str(el))
        Error(es)
    else:
        menu_teams()

def goto_map_from_game(): #Resets map to the normal state
    if len(archive.changes) >= 1:
        global teams, app, parametres
        z = deepcopy(archive.changes[0])
        [teams, app.field, parametres] = z
        archive.changes = []
    for el in teams.nm:
        teams.cords[el] = [-1, -1]
    menu_map()

def goto_game_from_end():
    for el in teams.nm: 
        teams.score[el], teams.curr[el] = teams.curr[el] - teams.score[el], teams.curr[el]
    menu_game()

def menu_settings(): #Menu for defining global gamefield parametres
    standart_menu()
    fr_nav = Frame(app.sw)
    fr_nav.pack()

    lb = Label(app.cw, text = "Width: ", font = MyFont)
    lb.grid(row = 1, column = 1)
    sc = tkinter.Spinbox(app.cw, values = (3, 6, 9, 12, 15, 18, 21, 24), font = MyFont)
    sc.grid(row = 1, column = 2)
    app.add_sp(sc)

    lb = Label(app.cw, text = "Height: ", font = MyFont)
    lb.grid(row = 2, column = 1)
    sc = tkinter.Spinbox(app.cw, values = (3, 6, 9, 12, 15, 18, 21, 24), font = MyFont)
    sc.grid(row = 2, column = 2)
    app.add_sp(sc)

    lb = Label(app.cw, text = "Cherry: ", font = MyFont)
    lb.grid(row = 3, column = 1)
    sc = tkinter.Spinbox(app.cw, values = range1(0, 9), font = MyFont)
    sc.grid(row = 3, column = 2)
    app.add_sp(sc)

    lb = Label(app.cw, text = "Apples: ", font = MyFont)
    lb.grid(row = 4, column = 1)
    sc = tkinter.Spinbox(app.cw, values = range1(0, 13), font = MyFont)
    sc.grid(row = 4, column = 2)
    app.add_sp(sc)

    lb = Label(app.cw, text = "Minimal distance: ", font = MyFont)
    lb.grid(row = 5, column = 1)
    sc = tkinter.Spinbox(app.cw, values = range1(1, 30), font = MyFont)
    sc.grid(row = 5, column = 2)
    app.add_sp(sc)

    var = tkinter.IntVar()
    cb = tkinter.Checkbutton(app.cw, text = lang.translate("Empty map"), variable = var,  onvalue="1", offvalue="0")
    cb.grid(row = 6, column = 1, columnspan = 2)
    app.cb_var = var

    bt = Button(fr_nav, text = parametres.SPACES + "Back" + parametres.SPACES, command = menu_teams)
    bt.grid(row = 6, column = 1)
    bt1 = Button(fr_nav, text = parametres.SPACES + "Next" + parametres.SPACES, command = com)
    bt1.grid(row = 6, column = 2)

    text = Message(app.bw, font = MyFont)#tkinter.Text(app.bw, font = MyFont, width = width, height = height)
    text.grid()
    app.add_es(text)

def menu_credits(): #My menu. Please don`t modify
    app.remove()
    f1 = Frame(root, bg = "blue", width = 600, height = 600)
    f2 = Frame(root, bg = "black")
    f3 = Frame(root, bg = "darkblue")
    f1.grid(row = 1, column = 1, columnspan = 2)
    f2.grid(row = 1, column = 3)
    f3.grid(row = 2, column = 1, columnspan = 3)
    c1 = tkinter.Canvas(f1, width = 600, height = 600)
    c1.create_image(250, 300, image = logo)
    c1.pack()
    message = Message(f2, font = MyFont, text = "Andrew Ishutin is a developer of this program.\nYou can send a message to:\nEmail: hazmozavr@gmail.com\nVk: https://vk.com/aishutin2002")
    message.pack()
    bt3 = Button(f3, text = "Back", command = menu_start)
    bt3.pack()
    app.add(f1)
    app.add(f2)
    app.add(f3)

def menu_map(): #Menu for previewing and changing the map
    standart_menu()
    c = tkinter.Canvas(app.cw, width = settings.width - 100, height = settings.height - 100)
    c.pack(expand = YES, fill = BOTH)   
    c.draw_gamefield(app.field)
    c.normalize()
    c.HotKeys("<Button-1>", replace)
    app.add_ca(c)
    app.add_fr_of_ca(app.cw)

    fr_nav = Frame(app.sw)
    fr_nav.pack()
    s = parametres.SPACES
    bt = Button(fr_nav, text = s + "Back" + s, command = menu_settings)
    bt.grid(row = 1, column = 1)
    bt2 = Button(app.bw, text = "Wall", command = lambda: app.change_brash("0"))
    bt2.grid(row = 1, column = 2)
    bt3 = Button(app.bw, text = "Food", command = lambda: app.change_brash("."))
    bt3.grid(row = 1, column = 3)
    bt4 = Button(app.bw, text = "Pacman", command = lambda: app.change_brash("<"))
    bt4.grid(row = 1, column = 4)
    bt5 = Button(app.bw, text = "Apple", command = lambda: app.change_brash("a"))
    bt5.grid(row = 1, column = 5) 
    bt6 = Button(app.bw, text = "Cherry", command = lambda: app.change_brash("c"))
    bt6.grid(row = 1, column = 6)
    bt7 = Button(fr_nav, text = s + "Next" + s, command = goto_menu_game)
    bt7.grid(row = 1, column = 2)
    bt8 = Button(fr_nav, text = s + "Load" + s, command = menu_continue_map)
    bt8.grid(row = 2, column = 1)
    bt9 = Button(fr_nav, text = s + "Save" + s, command = save_file)
    bt9.grid(row = 2, column = 2)

def menu_end(): #Menu for representing information in the end of the session
    standart_menu()   
    for el in teams.nm:
        teams.curr[el], teams.score[el] = teams.curr[el] + teams.score[el], teams.curr[el]
    sc = score_table(app.cw)
    sc.pack()

    fr_nav = Frame(app.sw)
    fr_nav.pack()

    Bt0 = Button(fr_nav, text = parametres.SPACES + "Back" + parametres.SPACES, command = goto_game_from_end)
    Bt0.grid(row = 1, column = 3)
    Bt = Button(fr_nav, text = parametres.SPACES + "Quit" + parametres.SPACES, command = menu_start)
    Bt.grid(row = 1, column = 1)
    Bt1 = Button(fr_nav, text = parametres.SPACES + "Save" + parametres.SPACES, command = save_game)
    Bt1.grid(row = 1, column = 2)

def menu_game(): #Menu for playing
    standart_menu()
    c = tkinter.Canvas(app.cw)
    c.pack(expand = YES, fill = BOTH)
    c.draw_gamefield(app.field)
    c.normalize()
    app.add_fr_of_ca(app.cw)
    app.add_ca(c)
    bt1 = Button(app.bw, text = "Back", command = goto_map_from_game)
    bt2 = Button(app.bw, text = "End game", command = menu_end)
    bt1.grid(row = 1, column = 1)
    bt2.grid(row = 1, column = 5)
    bt = Button(app.bw, text = "New round", command = new_game)
    bt.grid(row = 1, column = 4)
    bt3 = Button(app.bw, text = "Return", command = prev_change)
    bt3.grid(row = 1, column = 3)
    st = score_table(app.sw)
    st.pack()
    app.add_score(st)
    app.change_brash("<")
    c.HotKeys("<Button-1>", replace2)
    c.HotKeys("<Button-3>", replace3)

def menu_new_party(): #Menu for creating ew session
    standart_menu()
    font.nametofont('TkDefaultFont').configure(size = 20)
    teams.reset()
    fr_set = Frame(app.cw) #A frame for settings 
    fr_nav = Frame(app.sw) #A frame for navigation buttons
    fr_set.pack()
    fr_nav.pack()

    lb = Label(fr_set, text = "Number of teams: ")
    lb.grid(row = 1, column = 1, columnspan = 1)
    sc = tkinter.Spinbox(fr_set, values = range1(2, 9), font = MyFont)
    sc.grid(row = 1, column = 2, columnspan = 1)
    app.add_sp(sc)
    lb = Label(fr_set, text = "Cost of an apple: ")
    lb.grid(row = 2, column = 1, columnspan = 1)
    en = tkinter.Entry(fr_set, font = MyFont)
    en.insert(0, str(settings.apple))
    en.grid(row = 2, column = 2)
    app.add_sp(en)

    lb = Label(fr_set, text = "Do shields exists:")
    lb.grid(row = 3, column = 1, columnspan = 1)
    sp = tkinter.Spinbox(fr_set, values = (lang.translate("Yes"), lang.translate("No")), font = MyFont)
    sp.grid(row = 3, column = 2)
    app.add_sp(sp)

    bt0 = Button(fr_nav, text = parametres.SPACES + "Back" + parametres.SPACES, command = menu_start)
    bt0.grid(row = 5, column = 1)
    bt = Button(fr_nav, text = parametres.SPACES + "Next" + parametres.SPACES, command = goto_menu_teams)
    bt.grid(row = 5, column = 2)

    er = Message(app.bw, font = MyFont)
    er.grid(row = 6, column = 1, columnspan = 2)
    app.add_es(er)

def standart_menu(): #Standart menu template
    app.remove()
    fr_main = Frame()
    fr_main.pack(fill = BOTH, expand = 1)
    app.add(fr_main)
    fr_side = Frame(fr_main)
    fr_side.grid(row = 1, column = 2, rowspan = 2)
    fr_central = Frame(fr_main)
    fr_central.grid(row = 1, column = 1)
    fr_bottom = Frame(fr_main)
    fr_bottom.grid(row = 2, column = 1)
    ad = ad_vid(fr_side)
    ad.pack()
    app.cw = fr_central #central window
    app.bw = fr_bottom #bottom window
    app.sw = fr_side #side window. Please don`t use if you can

def menu_teams(): #Menu for creating teams
    standart_menu()
    n = settings.n
    lb1 = tkinter.Entry(app.cw, font = MyFont)
    lb2 = tkinter.Entry(app.cw, font = MyFont)
    lb1.insert(0, "Teams")
    lb2.insert(0, "Score")
    lb1.grid(row = 1, column = 1)
    lb2.grid(row = 1, column = 3)
    for i in range(n):
        lb1 = tkinter.Entry(app.cw, bg = teams.colors[i], font = MyFont)
        lb1.insert(0, "Name of team №" + str(i))
        lb1.grid(row = i + 2, column = 1)
        app.add_sp(lb1)
        lb1 = tkinter.Entry(app.cw, bg = teams.colors[i], font = MyFont)
        lb1.insert(0, "0")
        lb1.grid(row = i + 2, column = 3)
        app.add_sp(lb1) 
    fr_nav = Frame(app.sw)
    fr_nav.pack()
    bt = Button(fr_nav, text = parametres.SPACES + "Back" + parametres.SPACES, command = menu_new_party)
    bt.grid(row = n + 3, column = 1)
    bt2 = Button(fr_nav, text = parametres.SPACES + "Next" + parametres.SPACES, command = PrepareForGame)
    bt2.grid(row = n + 3, column = 3)
    text = Message(app.bw, font = MyFont)
    #    tkinter.Text width = width, height = height)
    text.grid(row = n + 4, column = 3)
    app.add_es(text)

def menu_start(): #Start menu
    app.remove()
    font.nametofont('TkDefaultFont').configure(size = 30)
    fr_main = Frame(bg = "pink")
    fr_main.pack()
    app.add(fr_main)
    fr = fr_main
    w1 = 15 #width of buttons
    h1 = 1  #height of buttons 
    bt = Button(fr, text = "New game", command = menu_new_party, width = w1, height = h1)
    bt.pack()
    bt2 = Button(fr, text = "Continue", command = load_game, width = w1, height = h1)
    bt2.pack()
    bt3 = Button(fr, text = "About", command = menu_credits, width = w1, height = h1)
    bt3.pack()
    bt4 = Button(fr, text = lang.lang_list[lang.curr], command = another_language, width = w1, height = h1)
    bt4.pack()
    app.lang_bt = bt4
    bt1 = Button(fr, text = "Quit", command = Quit, width = w1, height = h1)
    bt1.pack()

teams = team_data() #Storage for information about teams
source = "fields.sv"
#settings = prec(1366 - 15, 768 - 40, "3.5", source, 5) #GetSystemMetrics(0) - 15, GetSystemMetrics(1) - 40,
settings = prec(GetSystemMetrics(0) - 15, GetSystemMetrics(1) - 40, "3.6 alpha", source, 5) #
archive = hist()
#^Storage for const information^
width = 52
height = 5
BOTH = tkinter.BOTH
ALL = tkinter.ALL
YES = tkinter.YES
NW = tkinter.NW
END = tkinter.END
root = tkinter.Tk() #Main window
app = screen()
pc = tkinter.PhotoImage(file = "pacman.gif") 
ap = tkinter.PhotoImage(file = "apple.png") 
ch = tkinter.PhotoImage(file = "cherry.png")
logo = tkinter.PhotoImage(file = "KrechetBest.png") #My logo
theme = tkinter.PhotoImage(file = "Small Krechet.png")
root.title("Pacman v" + str(settings.version))
root.geometry(str(settings.width) + 'x' + str(settings.height))
parametres = param(0, 0, "         ")
lang = language()
font.nametofont('TkDefaultFont').configure(size = 30)
MyFont = font.Font(weight='bold', size = 20)
menu_start()
root.mainloop()