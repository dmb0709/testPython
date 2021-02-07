#!/usr/bin/env python3
''' Программа выводит название региона РФ по коду с номера автомобиля
вводим значение и получаем результат
'''
# Открываем файл на чтение
f = open('short.db', 'r')
d = {}
# Читаем файл в память
for line in f:
    kv = line.split(':')
    key = kv[0]
    value = kv[1]
    
    d[key]=value
   
# Здесь мы работаем с юзером
def vvod():
    print("Введите код региона! 0 - для выхода")
    code = input()
    if int(code) == 0:
        exit(0)
    print(d[code])
    vvod()
vvod()