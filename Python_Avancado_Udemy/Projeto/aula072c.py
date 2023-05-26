# Exercícios com funções

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(num):
    if num % 2 == 0:
        return f'O número {num} é PAR.'
    return f'O número {num} é ÍMPAR.'


print(par_impar(2))
print(par_impar(3))
