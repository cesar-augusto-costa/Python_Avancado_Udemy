"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]


print(salas, end='\n\n')
for sala in salas:
    print('A sala é', sala)
    for aluno in sala:
        print(aluno)
    print()


