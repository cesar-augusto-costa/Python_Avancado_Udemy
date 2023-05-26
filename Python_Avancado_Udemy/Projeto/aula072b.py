# Exercícios com funções

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par(num):
    return num % 2 == 0

num = 15

sit = par(num)
print(f'O número {num} é par? {sit}')
