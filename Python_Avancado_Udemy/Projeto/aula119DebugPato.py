# Rubber duck debugging
# Debug com Pato de Borracha
# book: O programador pragmatico

# Música para codar =)
# Everybody wants to rule the world - Tears for fears


# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

def listar(tarefas):
    print()
    if not tarefas:
        print('- Nenhuma tarefa para listar!')
        return
    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    # print(*tarefas, sep='\n')

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('- Nenhuma tarefa para desfazer!')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'{tarefa=} removida da lista de tarefas.')
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('- Nenhuma tarefa para refazer!')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    listar(tarefas)

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nada.')
        return
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    listar(tarefas)

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        print()
    elif tarefa == 'desfazer':
        print()
        desfazer(tarefas, tarefas_refazer)
        print()
    elif tarefa == 'refazer':
        print()
        refazer(tarefas, tarefas_refazer)
        print()
    elif tarefa == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        adicionar(tarefa, tarefas)
        print()