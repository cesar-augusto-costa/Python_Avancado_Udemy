"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

if num.isdigit():
    num_int = int(num)
    if num_int % 2 == 0:
        print(f'{num_int} é PAR')
    else:
        print(f'{num_int} é IMPAR')
else:
    print('Você não digitou um número inteiro.')

