# Combinations,Ppermutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

print(pessoas)
print('\n','Combinação', '\n')
print_iter(combinations(pessoas, 2))
print_iter(combinations(pessoas, 3))
print('permutação', '\n')
print_iter(permutations(pessoas, 2))
print_iter(permutations(pessoas, 3))