from tkinter import*
root = Tk()
f1 = Frame(root, bg = "blue", width = 600, height = 600)
f2 = Frame(root, bg = "black")
f3 = Frame(root, bg = "darkblue")
f1.grid(row = 1, column = 1, columnspan = 2)
f2.grid(row = 1, column = 3)
f3.grid(row = 2, column = 1, columnspan = 3)
me = PhotoImage(file = "KrechetBest.png")
c1 = Canvas(f1, width = 600, height = 600)
c1.create_image(250, 300, image = me)
c1.pack()
t2 = Text(f2)
t2.insert(END, "Andrew Ishutin is a developer of this programme. \nEmail: hazmozavr@gmail.com")
t2.pack()
bt3 = Button(f3, text = "Back", command = exit)
bt3.pack()
root.mainloop()