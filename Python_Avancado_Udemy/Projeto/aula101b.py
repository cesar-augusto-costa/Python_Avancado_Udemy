def soma(x):
    def adicao(y):
        return x + y
    yield adicao
 
 
def multiplica(x):
    def multiplicador(y):
        return x * y
    yield multiplicador
 
 
def criar_funcao(funcao, *args):
    return next(funcao(*args))
 
 
soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(12))
 
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(22))