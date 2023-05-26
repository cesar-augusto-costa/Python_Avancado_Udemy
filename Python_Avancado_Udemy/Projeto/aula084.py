# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

print(list(range(5)))

lista = []
for numero in range(8):
    lista.append(numero)
print(lista)

# List comprehension em Python

lista = [numero for numero in range(10)]
print(lista)

lista = [
    1 
    for numero in range(10)
]
print(lista)

lista = [
    numero * 2 
    for numero in range(10)
]
print(lista)
