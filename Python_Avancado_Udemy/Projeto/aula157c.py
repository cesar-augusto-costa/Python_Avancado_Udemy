# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum 
#enum.IntEnum
#enum.StrEnum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', 'CIMA'])
class Direcoes(enum.Enum):
  ESQUERDA = enum.auto()
  DIREITA = 2
  CIMA = enum.auto()

# membro = Classe(valor)
print(Direcoes(1), Direcoes(2), Direcoes(3))

# membro = Classe['chave']
print(Direcoes['ESQUERDA'], Direcoes['DIREITA'], Direcoes.CIMA)

# chave = Classe.chave.name
# valor = Classe.chave.value
print(Direcoes(1).value, Direcoes(1).name)
print(Direcoes['DIREITA'].value, Direcoes['DIREITA'].name)
print(Direcoes.CIMA.value, Direcoes.CIMA.name)

print()
def mover(direcao: Direcoes):
  if not isinstance(direcao, Direcoes):
    raise ValueError('Direção Inválida')
    
  print(f'Movendo para {direcao.name}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)

# mover('lado')
