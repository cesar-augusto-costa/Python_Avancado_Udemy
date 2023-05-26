# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# O número recebido como parametros.

def multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))