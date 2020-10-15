#!/usr/bin/env python3
from sys import argv


def kvadrat(x):
    a = float(x)
    print(' При стороне квадрата: ', a)
    print(' Периметр квадрата: ', 4 * a)
    print(' Площадь квадрата: ', round(a * a, 5))
    b = a * 2**(1/2)
    print(' Диагональ квадрата: ', round(b, 3))


if len(argv) > 1:
    kvadrat(argv[1])
else:
    x = input('Введите сторону квадрата:  ')
    kvadrat(x)
