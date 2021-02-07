#!/usr/bin/env python3
'''Программа печатает на экране текущее время и паралельно пишет в файл.'''
import time
f = open('text.txt', 'a')
raz = 2
i = 0
while 1 != raz:
    # time.sleep(0.01) замедляет выполнение
    now = time.strftime('%M_%S')
    raz = (int(time.strftime('%S')))
    print(str(now), end=' ! ')
    f.write(now + ' hop')
    i += 1
print('\n Было аж ' + str(i) + ' итераций')
