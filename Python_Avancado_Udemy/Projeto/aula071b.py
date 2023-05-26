"""
args - Argumentos não nomeados
* - *args (empacotamento)
"""

# Lembre-se de desempacotamento

def soma(*args):
    total = 0
    for numero in args:
        print(f'{total} + {numero}')
        total += numero
        print('Total', total)

soma(1,2,3,4,5,6)
