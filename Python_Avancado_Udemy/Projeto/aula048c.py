"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3  
lista = [10, 20, 30, 40]
print(lista)

lista.append(50)
print(lista)

removido = lista.pop() # retorna o removido
print(removido)
print(lista)

removido = lista.pop(1) # retorna o removido
print(removido)
print(lista)
