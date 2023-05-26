"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome == '' and idade == '':
    print('Desculpe, você deixou os campos vazios.')
elif nome == '':
    print('Desculpe, você deixou o campo nome vazio.')
elif idade == '':
    print('Desculpe, você deixou o campo idade vazio.')
elif not idade.isnumeric():
    print('Desculpe, idade não é um número inteiro.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {nome.count(" ")} espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

