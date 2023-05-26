def executa(funcao, *args):
    return funcao(*args)

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))
