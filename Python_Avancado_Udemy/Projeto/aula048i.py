"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# apelido do valor = valor

nome = 'Luiz'
# nome[0] = 'J' # erro - imutavel
outra_variavel = nome
nome = 'João'
print(nome)
print(outra_variavel)
