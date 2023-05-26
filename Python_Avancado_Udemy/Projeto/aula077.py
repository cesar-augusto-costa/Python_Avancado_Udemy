# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for i, pergunta in enumerate(perguntas):
    print(f'Pergunta {i+1}:', pergunta['Pergunta'])
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i+1}) {opcao}')
    
    escolha = input('- Escolha uma opção: ')
    
    acertou = False
    qtd_opcoes = len(opcoes)

    escolha_int = None
    if escolha.isdigit():
        escolha_int = int(escolha)
        if escolha_int > 0 and escolha_int <= qtd_opcoes:
            if opcoes[escolha_int-1] == pergunta['Resposta']:
                acertou = True
    if acertou:
        print('Resposta: Correta')
        qtd_acertos += 1
    else:
        print('Resposta: Errada')

    print('----------------\n')
print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')