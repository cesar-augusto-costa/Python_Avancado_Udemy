# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # metodo da classe
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    # factorie metodo
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

p1 = Pessoa.criar_com_50_anos('Helana')
print(p1.nome, p1.idade)

