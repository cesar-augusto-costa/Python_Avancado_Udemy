# Manipulando chaves e valores em dicionários

pessoa = {}

pessoa['nome'] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa)

pessoa['nome'] = 'Maria'

print(pessoa)

del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Chave não existe!')
else:
    print(pessoa['sobrenome'])