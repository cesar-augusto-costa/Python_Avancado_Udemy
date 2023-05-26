"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, msg, nome):
    return funcao(msg, nome)


v = executa(saudacao, 'Bom dia', 'Cesar')
print(v)
