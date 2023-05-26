# Empacotamento e Desempacotamento de dicionários
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

configuracoes = {
    'arg1': 1,
    'arg2': 2
}

mostro_argumentos_nomeados(**configuracoes)
