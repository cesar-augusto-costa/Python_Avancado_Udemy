from itertools import zip_longest

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

lista_soma = [
    x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)
]
print(lista_soma)
