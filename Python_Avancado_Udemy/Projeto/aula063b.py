"""
RE - Expressão Regular
"""
import re
import sys

cpf = '746.824.890-70'
cpf = '222.222.222-22'

cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    cpf
 )

entrada_e_sequencial = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

if entrada_e_sequencial:
    print('CPF inválido, dados sequenciais!')
    sys.exit()

nove_digitos = cpf_enviado[:9]
dez_digitos = cpf_enviado[:10]

contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = resultado_digito_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = resultado_digito_2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == cpf_gerado:
    print(f'{cpf} é válido.')
else:
    print(f'{cpf} inválido.')
