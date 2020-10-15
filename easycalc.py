#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from decimal import *
getcontext().prec = 30

a = Decimal(input('Введите первое число: '))
b = Decimal(input('Введите второе число: '))
oper = input('Введите операцию из +-*/ :')
if oper == '*':
    a = a * b
    print(a)
elif oper == '+':
    a = a + b
    print(a)
elif oper == '-':
    a = a - b
    print(a)
    print(type(a))
elif oper == '/':
    a = a / b
    print(a)
else:
    print('Операция не распознана!')
# print('hello world!')
