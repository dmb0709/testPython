#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from tkinter import *
root = Tk()
root.title("Графическая программа на Python")
root.geometry("600x600")
risovalca = Canvas()
# risovalca.fill

x = 1
while x <= 400:
    y = x = 2
    canvas = Canvas()
    canvas.create_rectangle(x, y, 105, 105)
    canvas.pack()
    x += 1
root.mainloop()
