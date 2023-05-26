# Empacotamento e Desempacotamento de dicionários
# kwargs - keyword arguments (argumentos nomeados)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.62
}

pessoa_completa = {
    **pessoa, **dados_pessoa, 'peso': 60
}

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(**pessoa_completa)
