#!/usr/bin/evn python3
#
from sys import argv
def stest(a):
	try:
		x = int(a)
	except ValueError:
		print('Тут ошибка. Нужно вводить числа!')
		quit()
	if x < 0:
		x = x * -1
	elif x == 1 or x == 2 or x == 3:
		print(f'Число {x} является простыvм.')
		quit()
	elif x == 0:
		print('Ноль тут вообще ни при чëм!')
		quit()
	d = 3
	while d*d <= x and x%d != 0:
		d += 2
	if x % d == 0:
	    print(f'Число {x} является составным, делитель {d}.')
	else :
		print(f'Число {x} является простым.')
if len(argv) >1:
		stest(argv[1])
per = input('Введите число на проверку: _')	
		
stest(per)