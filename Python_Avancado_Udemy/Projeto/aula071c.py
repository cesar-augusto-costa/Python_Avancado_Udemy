"""
args - Argumentos não nomeados
* - *args (empacotamento)
"""

# Lembre-se de desempacotamento

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma1 = soma(1,2,3,4,5,6)
print(soma1)

soma2 = soma(1,2,3)
print(soma2)

print(sum((1, 2, 3)))
