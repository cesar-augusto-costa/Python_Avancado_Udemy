# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.upper())
    print(letras)
    if 'C' and 'A' in letras:
        print('PARABÉNS')
        break
    