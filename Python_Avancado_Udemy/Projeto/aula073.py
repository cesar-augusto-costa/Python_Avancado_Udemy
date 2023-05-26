"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg):
    return msg

print(saudacao('Olá'))

saudacao_2 = saudacao

print(saudacao_2('Olá 2'))
