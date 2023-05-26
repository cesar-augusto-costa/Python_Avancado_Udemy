"""
Listas em Python (array de outras linguagens)
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE' # 5 CARACTERES (len)
lista = [] # list()
print(lista, type(lista))
print(bool([lista])) # False

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio', 1.2, []]
print(lista)
lista[2] = 'Maria'
print(lista[2].upper(), type(lista[2]))


