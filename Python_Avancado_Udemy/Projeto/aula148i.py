# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A:
    def __new__(cls, x):
        instancia = super().__new__(cls)
        # return object.__new__(A)
        return instancia

    def __init__(self, x) -> None:
        self.x = x
        print('Sou o init')

    def __repr__(self) -> str:
        return 'A()'

a = A(123)
# a = object.__new__(A)
# a.__init__()
print(a.x)