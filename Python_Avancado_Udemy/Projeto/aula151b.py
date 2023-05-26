# Funções decoradoras e decoradores com classes
# Composição

def adiciona_repr(cls):
    def repr(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = repr
    return cls

class Time:
    def __init__(self, nome):
        self.nome = nome   

class Planeta:
    def __init__(self, nome):
        self.nome = nome

Time = adiciona_repr(Time)

brasil = Time('Brasil')
portugal = Time('Portugal')

Planeta = adiciona_repr(Planeta)

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)