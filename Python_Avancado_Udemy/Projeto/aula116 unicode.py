# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# Criando arquivos com Python + Context Manager with
# # with open (context manager) e métodos úteis do TextIOWrapper

#  Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

#caminho completo
caminho_arquivo = 'C:\\Users\\Cesar_costa\\Desktop\\Python_Avancado_Udemy\\Python_Avancado_Udemy\\Projeto\\'
caminho_arquivo += 'aula116.txt'

#caminho atual
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()
with open(caminho_arquivo, 'w+') as arquivo:
    print('type(arquivo):', type(arquivo))
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0) #voltar o cursor
    print('read')
    print(arquivo.read())
   
    # lendo linha por linha
    arquivo.seek(0, 0)
    print('readline')
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    arquivo.seek(0, 0)
    print('readlines')
    for linha in arquivo.readlines():
        print(linha.strip())
    

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())








