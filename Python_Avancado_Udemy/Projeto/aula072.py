# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    result = 1
    for num in args:
        result *= num
    return result

total = multiplicar(2, 4, 8)
print(total)

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(num):
    if num % 2 == 0:
        return 'PAR'
    return 'ÍMPAR'

num = 15

sit = par_ou_impar(num)
print(f'O número {num} é {sit}')
