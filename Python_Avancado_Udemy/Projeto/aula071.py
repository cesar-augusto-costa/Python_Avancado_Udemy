"""
args - Argumentos não nomeados
* - *args (empacotamento)
"""

# Lembre-se de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(*args):
    print(args, type(args))
    args = list(args)
    print(args, type(args))

soma(1,2,3,4,5,6)
