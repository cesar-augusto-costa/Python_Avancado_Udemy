"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a # aponta pro mesmo local
lista_b.append('Cesar')
print(lista_a)
print(lista_b)
