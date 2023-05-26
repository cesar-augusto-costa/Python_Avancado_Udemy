"""
Calculadora com while
"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except Exception as error:
        print(error) 

    if numeros_validos is None:
        print( 'Um ou ambos os números são inválidos.')
        continue
    
    operadore_permitidos = '+-/*'

    if operador not in operadore_permitidos:
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        resultado = numero_1 + numero_2
    elif operador == '-':
        resultado = numero_1 - numero_2
    elif operador == '/':
        resultado = numero_1 / numero_2
    else:
        resultado = numero_1 * numero_2

    print(f'{numero_1} {operador} {numero_2} = {resultado:.2f}')

    sair = bool(input('Quer sair? [s]im: ').lower().startswith('s'))
    if sair:
        break


