# Problema dos parâmetros mutáveis em funções Python

def adiciona_cliente(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = []
adiciona_cliente('Luiz', cliente1)
adiciona_cliente('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_cliente('Helena')
adiciona_cliente('Maria', cliente2)
print(cliente2)

cliente3 = adiciona_cliente('Moreira')
adiciona_cliente('Vivi', cliente3)
print(cliente3)