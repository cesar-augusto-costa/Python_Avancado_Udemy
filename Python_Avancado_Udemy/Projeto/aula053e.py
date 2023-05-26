"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(f'{valor}', end='\t')
    print()

