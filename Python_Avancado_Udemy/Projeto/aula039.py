"""
Iterando strings com while
"""

nome = 'Luiz Otávio' # Iteráveis
tamanho_nome = len(nome)

novo_nome = ''
indice = 0

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += '*' + letra
    indice += 1
novo_nome += '*'
print(novo_nome)


