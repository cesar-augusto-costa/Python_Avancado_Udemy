"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor especifico.
Por padrão, funções Python retornam None
None = (Não Valor - não tem nada definido).
"""

def imprimir():
    print('Várias')

imprimir()

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Desconhecido'):
    print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()

