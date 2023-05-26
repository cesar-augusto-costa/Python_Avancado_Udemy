# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# São funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# Decoradores são "Syntax Sugar" (Açúcar Sintático)

# Função Decoradora
def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# Syntax Sugar
@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

invertida = inverte_string('123')
print(invertida)

