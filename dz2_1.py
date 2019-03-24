from tkinter import *
from random import choice

COLORS = ("snow", "linen", "PeachPuff", "cornsilk", "ivory", "azure",
          "white", "black", "gray", "navy", "blue", "cyan", "green",
          "yellow", "khaki", "gold", "RosyBrown", "sienna", "peru",
          "burlywood", "beige", "wheat", "tan", "brown", "salmon",
          "orange", "coral", "tomato", "red", "pink", "maroon",
          "violet", "plum", "orchid", "purple", "thistle")

def change(event, label):
    bg_txt = choice(COLORS)
    fg_txt = choice(COLORS)
    label.configure(bg = bg_txt, fg = fg_txt)

i = 0

def add(*args):
    global i
    i = i+1
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
    Txt = Label(root, text="label")
    Txt.grid(row=i, column=1, sticky=E+W+N+S)
    Butt1 = Button(root, text="button")
    Butt1.bind("<Button-1>", lambda event: change(event, Txt))
    Butt1.grid(row=i, column=0, sticky=E+W+N+S)


TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

Butt = Button(root, text="Add")
Butt.bind('<Button-1>', add)
Butt.grid(row=0, column=0, sticky=E+W)
Exit = Button(root, command=root.quit, text="Exit")
Exit.grid(row=0, column=1, sticky=E+W)

TKroot.mainloop()
print("Done")
root.destroy()
TKroot.destroy()
