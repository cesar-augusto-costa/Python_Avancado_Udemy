# Métodos em instâncias de classes Python

class Carro:
    def __init__(self, alguma_coisa='Sei lá'):
        self.nome = alguma_coisa

fusca = Carro('fusca')
print(fusca.nome)

nao_sei = Carro()
print(nao_sei.nome)