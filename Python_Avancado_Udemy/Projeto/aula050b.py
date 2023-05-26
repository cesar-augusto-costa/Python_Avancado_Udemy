"""
Exercício
Exiba os índices da lista
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for i in indices:
    print(i, lista[i])