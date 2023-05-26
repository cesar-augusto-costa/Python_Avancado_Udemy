lista = [
    x
    for x in range(3)
    for y in range(3)
]
print(lista)

lista = [
    x for y in range(3)
    for x in range(3)
]
print(lista)

lista = [
    letra for letra in 'Luiz'
]
print(lista)