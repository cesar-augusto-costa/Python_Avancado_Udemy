# Dictionary Comprehension e Set Comprehension
lista = [
    ('nome', 'Caneta Azul'),
    ('preco', 2.5),
    ('categoria', 'Escritório')
]
    

dc = {
    chave: valor
    for chave, valor in lista
}
print(dc)

dicionario = dict(lista)
print(dicionario)
