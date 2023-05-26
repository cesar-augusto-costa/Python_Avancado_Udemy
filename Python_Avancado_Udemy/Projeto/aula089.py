# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

print(dir(string))

if hasattr(string, metodo):
    print('Existe o método', metodo)
    # print(string.upper())
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
    print(string)


