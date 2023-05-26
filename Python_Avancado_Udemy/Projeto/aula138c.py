# Herança simples - Relações entre classes
# Associação - usa
# Agregação - tem
# Composição - É dono de
# Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print('Estou na classe PESSOA')
        print(
            self.__class__.__name__,
            '-',
            self.nome,
            self.sobrenome
        )

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(
            self.__class__.__name__,
            '-',
            self.nome,
            self.sobrenome
        )
class Aluno(Pessoa):
    cpf = '4321'

c1 = Cliente('Luiz', 'Otávio')
a1 = Aluno('Maria', 'Helena')

c1.falar_nome_classe()
print(c1.cpf)

a1.falar_nome_classe()
print(a1.cpf)

# help(Cliente)

