numeros = [1, 2, 3, 4, 5]
print(numeros)

novos_numeros = []
for numero in numeros:
    novos_numeros.append(numero * 4)
print(novos_numeros)

# List Comprehension
novos_numeros = [numero / 2 for numero in novos_numeros]
print(novos_numeros)

# Condicionais
novos_numeros = [
    numero
    if numero != 3 else 30
    for numero in numeros
    if numero % 2 != 0
]
print(novos_numeros)

# string
string = 'Otávio Miranda'
nova_string = [letra for letra in string]
print(nova_string)

numero_letras = 1
nova_string = '.'.join([
    string[indice:indice + numero_letras]
    for indice in range(0, len(string), numero_letras)
])
print(nova_string)

nomes = ['luiz', 'MARIA', 'Helena', 'Joana']
novos_nomes = [
    nome.lower().title()
    for nome in nomes
]
print(novos_nomes)

novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(novos_nomes)

numeros = [(numero, numero ** 2) for numero in range(10)]
print(numeros)
# FLAT
flat = [y for x in numeros for y in x] 
print(flat)
