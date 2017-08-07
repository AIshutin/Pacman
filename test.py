import random
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import*

def change_font_family(query, named_font):
    named_font.configure(family=random.choice(font.families()))

root = parent = Tk()
root.title("Change font demo")

# standard named font (everything that uses it will change)
font.nametofont('TkDefaultFont').configure(size=5) # tiny

# you can use your own font
MyFont = font.Font(weight='bold')

query = StringVar()
ttk.Entry(parent, textvariable=query, font=MyFont).grid() # set font directly
ttk.Button(parent, text='Change Font Family',  style='TButton', # or use style
           command=lambda: change_font_family(query, MyFont)).grid()
query.set("The quick brown fox...")

# change font that widgets with 'TButton' style use
root.after(3000, lambda: ttk.Style().configure('TButton', font=MyFont))
# change font size for everything that uses MyFont
root.after(5000, lambda: MyFont.configure(size=48)) # in 5 seconds
root.mainloop()