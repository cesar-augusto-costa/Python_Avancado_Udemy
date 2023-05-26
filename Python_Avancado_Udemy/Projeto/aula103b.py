# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# São funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# Função Decoradora
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorado')
        return resultado
    return interna

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

def inverte_string(string):
    return string[::-1]

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro(123)
print(invertida)

