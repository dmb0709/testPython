#!/usr/bin/env python3
''' Программа выводит название региона РФ по коду с номера автомобиля
вводим значение и получаем результат
'''
# Открываем файл на чтение
f = open('short.db', 'r')
d = {}
for line in f:
    kv = line.split(':')
    key = kv[0]
    value = kv[1]
    
    d[key]=value
    
print("hello world")
print(f)
print(d['25'])
