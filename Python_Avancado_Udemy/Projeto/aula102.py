# Variáveis livres + nonlocal (locals , globals)

print('Global:', globals())
def fora(x):
    a = x
    print('Local Fora: ', locals())
    def dentro():
        print('Local Dentro: ',locals()) 
        print('Livre: ', dentro.__code__.co_freevars)
        # Variavel Livre
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())
