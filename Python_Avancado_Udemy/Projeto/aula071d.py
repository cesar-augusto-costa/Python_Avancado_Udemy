"""
args - Argumentos não nomeados
* - *args (empacotamento)
"""

# Lembre-se de desempacotamento

def soma(*args):
    print(args) # mostra a tupla
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 2, 3, 4

soma1 = soma(*numeros) # desempacotamento
print(soma1)

print(sum((numeros)))
