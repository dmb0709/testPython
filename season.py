#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sys import argv
import sys 
def seazon(x):
    try:
        a = int(x)
    except ValueError:
        print('Что за фигня? ', x)
        exit()
    if 1 > a or a > 12:
        print('FATAL ERROR!!!!!')
        sys.exit()
    
    if 3<=a and a <= 5:
        print('Весна ')
    elif 6 <= a <= 8:
        print('Лето ')
    elif 9 <= a <= 11:
        print('Осень ')
    elif a == 12 or a == 1 or a == 2:
        print('Зима ')
        #print(a)
    else:
        print('Не то  число ты ввёл!!!')
if len(argv) > 1:
    seazon(argv[1])
else:
    monf = input('Введите номер месяца от 1 до 12:  ')
    seazon(monf)
