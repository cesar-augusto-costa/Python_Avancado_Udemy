# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero') 
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" envido.'
        )
    return True
__name__
def divide(n, d): 
    nao_aceita_zero(d)
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    return n / d   

print(divide(8, '0')) 

