# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print('SET:', item)
    elif isinstance(item, str):
        print('STR:', item.upper())
    elif isinstance(item, bool):
        print('BOOL:', item)
    elif isinstance(item, (int, float)):
        print('NUM:', item, item * 2) 
    elif isinstance(item, (tuple)):
        print('TUPLE:', item)
    elif isinstance(item, (list)):
        print('LISTA:', item)
    elif isinstance(item, (dict)):
        print('DICIONARIO:', item)
    else:
        print('OUTRO:', item)

print(lista)