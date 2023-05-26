# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy)
# deepcopy - retorna uma cópia profunda

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}
# d2 = copy.copy(d1) # shallow copy
d2 = copy.deepcopy(d1)
d2['c1'] = 1000
d2['l1'][1] = 10
print(d1)
print(d2)
