from dados import produtos

import copy
from copy import deepcopy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

produtos_ordenados_por_nome = sorted(
    novos_produtos,
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenados_por_preco = sorted(
    novos_produtos,
    key=lambda p: p['preco']
)

print(*produtos, sep='\n', end='\n\n')
print(*novos_produtos, sep='\n', end='\n\n')
print(*produtos_ordenados_por_nome, sep='\n', end='\n\n')
print(*produtos_ordenados_por_preco, sep='\n', end='\n\n')
