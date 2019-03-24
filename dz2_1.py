from tkinter import *
from random import random
from math import fabs

def change(event, label):
    red = int(random()*16)
    green = int(random()*16)
    blue = int(random()*16)
    colors_bg = [red,green,blue]
    bg_txt = '#%0x%0x%0x' % (red, green, blue)
    red1 = int(random()*16)
    green1 = int(random()*16)
    blue1 = int(random()*16)
    colors_fg = [red1,green1,blue1]
    for i in range(3):
        if (fabs(colors_bg[i] - colors_fg[i]) % 16) < 3:
            colors_fg[i] = (colors_fg[i] + 5) % 16           
    fg_txt = '#%0x%0x%0x' % (colors_fg[0], colors_fg[1], colors_fg[2])
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
