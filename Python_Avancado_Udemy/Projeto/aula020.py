primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior '
        f'do que {segundo_valor=}'
    )
elif primeiro_valor < segundo_valor:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
else:
    print('Os dois valores são iguais.')
