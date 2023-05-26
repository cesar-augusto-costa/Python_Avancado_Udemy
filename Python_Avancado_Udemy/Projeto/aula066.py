"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeado tem nome com sinal de igual

Argumento posicional

Argumento não nomeado recebe apenas o argumento (valor)
""" 
def soma(x, y):
    # Definição
    print(f'{x=} e y={y} | x + y = {x + y}')

soma(1, 2)
soma(2, 1)
soma(y=3, x=4)



