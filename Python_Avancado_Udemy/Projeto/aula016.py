# if /      elif        / else
# se /      se não se   / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada.lower() == 'entrar':
    print('Você entrou no sistema')
elif entrada.lower() == 'sair':
    print('Você saiu do sistema')
else:
    print('Opção inválida!')

