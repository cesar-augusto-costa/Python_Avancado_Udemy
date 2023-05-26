"""
split e join com list e str
split - divide uma string
join - une strings
"""
frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(',')

for i, item in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()

print(lista_frases)


