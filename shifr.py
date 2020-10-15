#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sys import argv


def koding(pkey, opentext):
    slovo = ''
    i = 0
    while i != len(opentext):
        bukva = chr(ord(opentext[i])+ord(pkey[2]))
        slovo = slovo + bukva
        print(bukva, end='')
        i += 1
    print(f'\n\nРезультат шифрования: {slovo}')


def enkoding(pkey, cryptotext):
    pass


# Операции ввода ключа и текста.
if argv[1] == '--code' or argv[1] == '-c':
    koding(argv[2], argv[3])
elif argv[1] == '--encrypt' or argv[1] == '-en':
    # тут должно быть чтение из файла text.cry
    # и передача его в качестве второго аргумента.
    enkoding(argv[2], 'чтение из файла')
