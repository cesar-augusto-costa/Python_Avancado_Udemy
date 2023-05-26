# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('João', 35)
print(vars(p1))
p1.nome = 'José'
print(vars(p1))
del p1.nome
p1.__dict__['caneta'] = 'azul'
vars(p1)['azul'] = 'caneta'
print(p1.__dict__)
del p1.__dict__['caneta']
del vars(p1)['azul']
print(p1.__dict__)

