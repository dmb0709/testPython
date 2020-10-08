t = 'Значит можно шифровать что-то серьëзное!!! ура!'
k = 'password'
i = 0
slovo = ''
result =''
while i != len(t):
    bukva = chr(ord(t[i])+ord(k[3]))
    slovo = slovo + bukva
    print(bukva, end='')
    i += 1
print(f'\n\nРезультат шифрования: {slovo}')
# теперь расшифровка
j = 0
#print(slovo)
while j != len(slovo):
    bukva2 = chr(ord(slovo[j]) - ord(k[3]))
    result = result + bukva2
    j += 1
print(result)