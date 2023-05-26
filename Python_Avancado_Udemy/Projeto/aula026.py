"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caracter)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal -> + ou -
Ex.: 0>-100,.1f

Conversion Flags - !r !s !a
!r = __repr__
!s = __str__
!a =
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}')
print(f'{variavel:^10}')
print(f'{variavel:-^10}')
print(f'{6000999.475:+,.2f}')
print(f'{6000999.475:0>15,.2f}')
print(f'{6000999.475:0>+15,.2f}')
print(f'{6000999.475:0=+15,.2f}')
print(f'O hexadecimal de 1500 é {150:04X}')

