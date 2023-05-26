"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeado tem nome com sinal de igual

Argumento posicional é Argumento não nomeado

Argumento não nomeado recebe apenas o argumento (valor)
""" 
def soma(x, y, z):
    # Definição
    print(f'{x=}, {y=} e {z=} | x + y + z = {x + y + z}')

soma(1, 2, 3)
soma(y=2, z=3, x=1)
soma(1, y=2, z=5)


