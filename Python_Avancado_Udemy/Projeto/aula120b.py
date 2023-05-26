# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Luiz'
p1.sobrenome = 'Otávio'

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Joana'

print(p1)
print()
print(p1.nome)
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)
