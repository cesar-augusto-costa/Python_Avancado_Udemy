# Try, except, else e finally

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1')
    c = a / b
    print('Linha 2')
    print('Linha 3'[10])
except ZeroDivisionError as e:
    print('ERRO: Não é possível dividir por zero.')
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Variável não está definada.')
except (TypeError, IndexError) as error:
    print('TypeError or IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('Erro Desconhecido.')
print('Continuar')
