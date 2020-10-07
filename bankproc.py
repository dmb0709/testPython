#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#from sys import argv
def procent (babki = 0, years = 0):
    i = 1
    while i <= years:
        babki = babki + babki * 0.1
        #print(i)
        #print(round(babki, 2))
        print(f'Год {i} сумма на счету {round(babki, 2)} рублей.')
        i += 1
years = int(input('Cколько лет копить? __ '))
if years > 150:
    print('Ты столько не проживёшь!!!')
    quit()
babki = int(input('Сколько денег, нищеброд? __ '))
procent(babki, years)
