# Métodos úteis dos dicionários em Python
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
    'idade': 18
}
print(p1)
print(p1.get('sobrenome'))
print()
nome = p1.pop('nome')
print(nome)
print(p1)
print()
ultimo_item = p1.popitem()
print(ultimo_item)
print(p1)
print()
p1.update({
    'nome': 'Cesar',
    'sobrenome': 'Costa',
    'idade': 18
})
print(p1)
print(p1)
tupla = ('nome', 'Cesinha'),
p1.update(tupla)
print(p1)
p1.update(
    (
    ('nome', 'Shaolin'),
    ('idade', 29)
    )
)
print(p1)
lista = [['nome', 'Cesinha'],]
p1.update(lista)
print(p1)
