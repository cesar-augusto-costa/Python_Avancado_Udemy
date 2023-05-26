# Métodos em instâncias de classes Python

class Carro:
    def __init__(this, nome):
        this.nome = nome
    def acelerar(esse):
        print(f'{esse.nome} está acelerando.')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome = 'Celta')
print(celta.nome)
celta.acelerar()
