"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Luiz Otávio'
print(string[3])
# string[3] = 's' #ERRO
print(string)
 
outra_variavel = f'{string[:3]}s{string[4:]}'
print(outra_variavel)

