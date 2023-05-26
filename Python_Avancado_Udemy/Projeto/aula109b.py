# Combinations,Ppermutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino', 'unisex'],
    ['algodão', 'poliester']
]

print(camisetas)
print('\n','Combinação', '\n')

print_iter(product(*camisetas))

