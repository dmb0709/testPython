#!/usr/bin/evn python3
from sys import argv


def stest(a):
    ''' Функция проверяет число на простоту. Сначала приводим число к инту,
    и передаëм в новую переменную так как из строки вызова может придти
    список или кортеж. хз. '''
    try:
        x = int(a)
    except ValueError:
        print('Тут ошибка. Нужно вводить числа!')
        quit()
# Проверка на корректность пришедшего числа.
    if x < 0:
        # Отрицательное переводим в положительное.
        x = x * -1
    elif x == 1 or x == 2 or x == 3:
        print(f'Число {x} является простыvм.')
        quit()
    elif x == 0:
        print('Ноль тут вообще ни при чëм!')
        quit()
    elif x % 2 == 0 or x % 3 == 0:
        print('Число составное!!')
        quit()
    d = 3
    while (d * d <= x) and (x % d != 0):
        d += 2
    if x % d == 0:
        print(f'Число {x} является составным, делитель {d}.')
    else:
        print(f'Число {x} является простым.')


# Ввод чисел из разных источников
if len(argv) > 1:
    stest(argv[1])
else:
    chislo = input('Введите число на проверку: _')
    stest(chislo)
