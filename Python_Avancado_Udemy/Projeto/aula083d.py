# Empacotamento e Desempacotamento de dicionários
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)
    print('Não Nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
