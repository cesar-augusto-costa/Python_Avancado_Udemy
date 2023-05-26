"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite somente a hora sem os minutos (0-23): ')

try:
    hora_int = int(hora)
    if hora_int < 0 or hora_int > 23:
        print('Você digitou um horário inválido.')
    elif hora_int < 12:
        print('Bom dia')
    elif hora_int < 18:
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('Você não digitou um número inteiro.')

