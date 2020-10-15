#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from tkinter import *
root = Tk()
root.title("Графическая программа на Python")
root.geometry("600x600")
risovalca = Canvas()
# risovalca.fill
canvas = Canvas()
canvas.create_line(15, 25, 200, 25)
canvas.create_rectangle(100, 100, 105, 105)
canvas.pack()
root.mainloop()
