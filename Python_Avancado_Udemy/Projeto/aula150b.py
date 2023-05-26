# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def MyContextManager(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    except Exception as error:
        print('Erro:', error)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with MyContextManager('aula150.txt', 'w') as arquivo:
    print('WITH', arquivo)
    arquivo.write('Linha 1\r\n')  
    arquivo.write('Linha 2\r\n', 123)



