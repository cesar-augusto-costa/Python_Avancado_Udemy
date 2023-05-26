# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}
d2 = d1.copy()
d2['c1'] = 1000
d2['l1'][1] = 10
print(d1)
print(d2)
