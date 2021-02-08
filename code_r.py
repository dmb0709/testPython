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
    print('\033[1m' + "Введите код региона! 0 - для выхода" + '\033[0m')
    code = input()
    if code == '0':
        exit(0)
    exist_key = code in d
    if exist_key == False:
        print('\033[37m\033[41m' + 'Такого кода в базе нет!' + '\033[0m')
        vvod()

    print(d[code])
    vvod()


vvod()
