# Generator expression iterables e iterators em Python
# Generator não tem indice nem len()
# sys.getsizeof(): saber o tamanho em memória

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
lista =  [n for n in range(1000000)]
generator = (n for n in range(1000000))
print('lista:', sys.getsizeof(lista), 'bytes')
print('generator:', sys.getsizeof(generator), 'bytes')

print(next(generator))

for n in generator:
    print(n)
