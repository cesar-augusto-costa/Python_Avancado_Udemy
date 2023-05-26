from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = []
produtos_ordenados_por_nome = []
produtos_ordenados_por_preco = []
 
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in produtos
]
 
produtos.sort(key=lambda item: item['nome'], reverse=True)
for item in produtos:
    produtos_ordenados_por_nome.append(item)
 
produtos.sort(key=lambda item: item['preco'])
for item in produtos:
    produtos_ordenados_por_preco.append(item)

print(*produtos, sep='\n', end='\n\n')
print(*novos_produtos, sep='\n', end='\n\n')
print(*produtos_ordenados_por_nome, sep='\n', end='\n\n')
print(*produtos_ordenados_por_preco, sep='\n', end='\n\n')
