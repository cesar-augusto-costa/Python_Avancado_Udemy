# try, except, else e finally

try:
    print('Abrir Arquivo')
    8/0
except ZeroDivisionError as e:
    print('Erro: Divisão por zero')
    print(e.__class__.__name__)
    print(e)
except IndexError as error:
    print('IndexError')

except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('Fechar Arquivo')
