# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# 🟢 *args (ilimitado de argumentos posicionais)
print('args')

def soma(*args):
    print(sum(args))

soma(1)
soma(1, 0)

# 🟢 **kwargs (ilimitado de argumentos nomeados)
print('kwargs')

def soma(**kwargs):
    soma = 0
    for valor in kwargs.values():
        soma += valor
    print(soma)

soma(a=1, b=2)
soma(a=1, b=2, c=3)

# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
print('Positional-only Parameters')

def soma(a, b, /):
    print(a + b)

soma(1, 2)

def soma(a, b, /, x, y):
    print(a + b + x + y)

soma(1, 2, 3, y=4)

# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
print('Keyword-Only Arguments')

def soma(a, b, *, c):
    print(a + b + c)

soma(1, 2, c=3)
soma(1, b=2, c=3)


# 🟢 UNIAO DE (/) E (*)
print('UNIAO DE (/) E (*)')

def soma(a, b, /, *, c):
    print(a + b + c)

soma(1, 2, c=3)

# 🟢 OUTRO
print('OUTRO')

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)

soma(1, 2, c=3, nome='teste')
