# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]
print(*produtos, sep='\n')

novos_produtos = [
    produto 
    for produto in produtos
]
print(novos_produtos)

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco'] * 1.1} 
    for produto in produtos
]
print(novos_produtos)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    for produto in produtos
]
print(novos_produtos)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(novos_produtos)
