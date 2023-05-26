"""
Faça uma lista de comprar com listas.
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista = list()
lista = []
while True:
    print()
    print('LISTA DE COMPRAS')
    print()
    print('Selecione uma opção ?')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
    opcao = opcao.strip().lower()[0]
    os.system('cls')
    if opcao == 'i':
        lista.append(input('item da lista de compra: '))
    elif opcao == 'a':
        indice = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice)
            lista.pop(indice)
        except ValueError:
            print('ERRO. Digite um número inteiro.')
        except IndexError:
            print('ERRO. Índice não existe.')
        except Exception:
            print('Erro desconhecido.')
        finally:
            print('Não foi possível apagar este índice!')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar!')
        else:
            for i, item in enumerate(lista):
                print(i, item)
    elif opcao == 's':
        break
    else:
        print('Opção Inválida!')


