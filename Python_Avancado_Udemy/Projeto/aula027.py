"""
String é iterável

-> Fatiamento de Strings
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[0:3])
print(variavel[:3])
print(variavel[4:9])
print(variavel[4:])

print('-' * 10)

print(len(variavel))

print(variavel[::])
print(variavel[0:len(variavel):1])

print(variavel[0:9:2])

print(variavel[::-1])
print(variavel[-1::-1])
print(variavel[-1:-10:-1])

print(variavel[-1:-10:-2])









