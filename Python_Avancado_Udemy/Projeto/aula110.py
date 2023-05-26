# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = ['a', 'a', 'b', 'b', 'c', 'a']
grupos = groupby(sorted(alunos))

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))
