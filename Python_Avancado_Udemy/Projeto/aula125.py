# Atributos de classe

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 2000
    
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
        # return Pessoa.ano_atual - self.idade

print(Pessoa.ano_atual)

p1 = Pessoa('João', 29)
p2 = Pessoa('Helena', 12)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

Pessoa.ano_atual = 2050
print()

print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
