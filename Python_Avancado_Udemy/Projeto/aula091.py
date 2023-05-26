# Introdução ao Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1 # Pausar
    print('Continuando...')
    yield 2 # Pausar
    return 'ACABOU'


gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)




