#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from tkinter import *
from time import sleep
root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x400")


def dvijenie(x, y):
    while x < 100:
        canvas = Canvas()
        canvas.create_rectangle(x, y, 105, 105)
        canvas.pack()
        sleep(0.1)
        x += 1


dvijenie(10, 10)
root.mainloop()
