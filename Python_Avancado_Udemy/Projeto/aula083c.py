# Empacotamento e Desempacotamento de dicionários

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

print(pessoa_completa)