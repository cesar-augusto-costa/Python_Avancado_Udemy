# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Atributos que começar com um ou dois underlines _ ou __
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__ (self, cor):
        self.cor_tinta = cor
        self._cor = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

def mostrar(caneta):
    return caneta.cor

caneta = Caneta('Azul')


mostrar(caneta)
print()
print(mostrar(caneta))

# getter -> obter valor
print(caneta.cor)

# ERRO é um metodo
# caneta.cor = 'Rosa'

print(caneta.cor)





 