"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Bom dia')

print(s1('Luiz'))
print(s2('Otávio'))

