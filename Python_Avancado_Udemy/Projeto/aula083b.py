# Desempacotamento de dicionários

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

a, b = pessoa
print(a, b)

a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)

(a1, a2), b = pessoa.items()
print(a1, a2)
print(b)

print()
for chave, valor in pessoa.items():
    print(chave, valor)

