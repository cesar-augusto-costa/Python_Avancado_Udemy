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
        print('- Nenhuma tarefa para listar!', end='\n\n')
        return
    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    # print(*tarefas, sep='\n')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('- Nenhuma tarefa para desfazer!', end='\n\n')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'{tarefa=} removida da lista de tarefas.')
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('- Nenhuma tarefa para refazer!', end='\n\n')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    listar(tarefas)

def adicionar(tarefa, tarefas):
    
    tarefa = tarefa.strip()
    print()
    if not tarefa:
        print('Você não digitou nada.', end='\n\n')
        return
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    listar(tarefas)

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer e clear')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls' if os.name == 'nt' else 'clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']

    comando()
