# O que é JSON ?
# https://www.youtube.com/watch?v=XmCrArtfjaQ

# salvando dados do python para JSON

import json

with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))

print(pessoa['nome'])