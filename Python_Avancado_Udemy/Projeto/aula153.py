# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone
    
    def __call__(self, nome, *args, **kwds):
        print(nome, ', chamando: ', self.phone, sep='')
        return 123

call1 = CallMe('19991911666')

retorno = call1('Luiz Otávio')

print(retorno)
