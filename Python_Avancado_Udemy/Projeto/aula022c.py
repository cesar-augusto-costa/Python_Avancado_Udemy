entrada = input('[E]ntrar [S]air: ')

if entrada == 'E' or entrada == 'e':
    print('Entrar')
    usuario_digitado = input('Usuário: ')
    usuario_permitido = 'Luiz'
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'
    if usuario_digitado == usuario_permitido and senha_digitada == senha_permitida:
        print('Entrando')
    else:
        print('Usuário ou Senha Inválido!')
else:
    print('Sair')