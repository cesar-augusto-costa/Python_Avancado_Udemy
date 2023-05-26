# Yield from

def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    print('Acabou gen1')

def gen2(gen=None):
    print('Começou gen2')
    if gen is not None:
        yield from gen()
    yield 3
    yield 4
    print('Acabou gen2')

def gen3():
    print('Começou gen3')
    yield 10
    yield 20
    print('Acabou gen3')

g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()

for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
