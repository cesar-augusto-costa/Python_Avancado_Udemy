def soma(x, y):
    return x + y
 
 
def multiplica(x, y):
    return x * y
 
 
def criar_funcao(funcao, *args):
    return funcao(*args)
 
 
soma_com_cinco = lambda x:criar_funcao(soma, 5, x)
multiplica_por_dez = lambda x:criar_funcao(multiplica, 10, x)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))