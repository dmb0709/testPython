#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' Программа выводит название региона РФ по коду с номера автомобиля
вводим значение и получаем результат
'''
# Открываем файл на чтение
f = open('short.db', 'r', encoding='UTF-8')

d = {}
# Читаем файл в память
for line in f:
    kv = line.split(':')
    key = kv[0]
    value = kv[1]

    d[key] = value


def vvod():
    # Здесь мы работаем с юзером
    print("Введите код региона! 0 - для выхода")
    code = input()
    if code == '0':
        exit(0)
    exist_key = code in d
    if exist_key == False:
        print('Такого кода в базе нет!')
        vvod()

    print(d[code])
    vvod()


vvod()
