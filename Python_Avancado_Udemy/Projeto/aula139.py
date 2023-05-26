# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MinhaString(str):
    def upper(self):
        # return 'ABC' # sobreposição
        print('CHAMOU UPPER')
        print(super(MinhaString, self).upper())
        print('DEPOIS DO UPPER')
        # return super().upper()

string = MinhaString('Luiz')

print(string)

string.upper()


