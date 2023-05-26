# Decoradores com parâmetros

def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

def bla(a, b, c):
    print(a, b, c)
    return decoradora

@bla(1, 2, 3)
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
