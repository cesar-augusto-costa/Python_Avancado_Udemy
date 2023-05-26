# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1.union(s2)
print(s3)
s3 = s1 | s2
print(s3)

s3 = s1.intersection(s2)
print(s3)
s3 = s1 & s2
print(s3)

s3 = s1.difference(s2)
print(s3)
s3 = s1 - s2
print(s3)

s3 = s2.difference(s1)
print(s3)
s3 = s2 - s1
print(s3)

s3 = s1.symmetric_difference(s2)
print(s3)
s3 = s1 ^ s2
print(s3)

s3 = s2.symmetric_difference(s1)
print(s3)
s3 = s2 ^ s1
print(s3)

