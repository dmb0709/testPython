#!/usr/bin/env python3
from sys import argv


def god(x):
    if x % 4 == 0:
        print('Год високосный.')
    else:
        print('Год не високосный.')


if len(argv) > 1:
    god(int(argv[1]))
else:
    a = int(input('Введите год для проверки:  '))
    god(a)
