"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""
carro = 'Tesla'
ano = 2020
preco = 99500.69
variavel = 'O carro %s de %i vale R$ %.2f quase R$ %d' % (carro, ano, preco, preco)
print(variavel)