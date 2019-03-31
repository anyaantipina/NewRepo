#!/usr/bin/env python3
'''
Домашнее задание по 05_WidgetsAndCollaborative
'''
#ПРИМЕЧАНИЕ: почему-то команда os.path.dirname(sys.argv[0]) работает хорошо
#если запускать из idle3. Из командной строки она выдает пустую строку.

from tkinter import *
import os

TKRoot = Tk()
TKRoot.columnconfigure(0, weight=1)
TKRoot.rowconfigure(0, weight=1)
root = Frame(TKRoot)
root.grid(column=0, row=0, sticky=E+W+S+N)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

def FaceSelect(*args):
    filename = L.selection_get()
    index = PreferredNames.index(filename)
    I["image"]=Images[Names[index]]

Names = []
PreferredNames = []
location = os.path.dirname(sys.argv[0])
for file in os.listdir(location):
    if file.endswith(".png"):
        filename = file[0:len(file)-4]
        full_filename = location + '/' + filename + '.txt'
        if os.path.exists(full_filename):
            file_txt = open(full_filename, 'rb')
            decode_file_txt = ''
            for symbol in file_txt:
                new = symbol.decode('cp1252')
                decode_file_txt += new
            preferred_name = decode_file_txt
            PreferredNames.append(preferred_name)
        else:
            print('for ' + file + ' there is no ' + filename + '.txt')
            PreferredNames.append(file)
        Names.append(file)
       
Images = {k:PhotoImage(file=k) for k in Names}
Name = StringVar(value=PreferredNames)

L = Listbox(root, listvariable=Name)
L.grid(column=0, row=0, sticky=E+W+N)
L.bind('<<ListboxSelect>>', FaceSelect)
L.selection_set(0)
I = Label(root)
I.grid(row=0, column=1, sticky=E+W+S+N)
FaceSelect()

TKRoot.mainloop()
