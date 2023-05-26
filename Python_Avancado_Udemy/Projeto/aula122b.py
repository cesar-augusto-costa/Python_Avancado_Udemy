# Métodos em instâncias de classes Python

# Classe é o Molde (geralmente sem dados)
# Instância da Class (objeto) - tem os dados
# uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome} está acelerando.')

fusca = Carro('Fusca')

Carro.acelerar(fusca)

celta = Carro(nome = 'Celta')

Carro.acelerar(celta)
