frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
        'Python foi criado por Guido Van Rossum.'

i = 0
tamanho_frase = len(frase)


letra_apareceu_mais = ''
qtd_letra_apareceu_mais = 0

while i < tamanho_frase:
    letra_atual = frase[i]
    qtd_letra_apareceu = frase.count(letra_atual)
    i += 1
    if letra_atual == ' ':
        continue
    if qtd_letra_apareceu_mais < qtd_letra_apareceu:
        qtd_letra_apareceu_mais = qtd_letra_apareceu
        letra_apareceu_mais = letra_atual
print(
    'A letra que apareceu mais vezes foi a letra '
    f'"{letra_apareceu_mais}" que apareceu '
    f'{qtd_letra_apareceu_mais} vezes.'
)

