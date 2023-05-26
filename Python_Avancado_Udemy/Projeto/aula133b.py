# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       DEVE ser usado dentro da classe
#       ou com suas subclasses.
# __ (dois underlines) = private
#       só DEVE ser usado na classe em que foi
#       declarado.
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
    
    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        return 'metodo_puclic'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

f = Foo()

print(f.metodo_publico())

