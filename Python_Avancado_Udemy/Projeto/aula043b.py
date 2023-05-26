senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    repeticoes += 1
    if repeticoes == 4:
        print('Senha Bloqueada!')
        break
    senha_digitada = input(f'Sua senha ({repeticoes}ªx): ')
else:
    print('Entrou')
