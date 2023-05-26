# YOUTUBE
# Manipulando caminhos, pastas e arquivos no Python com pathlib

from pathlib import Path

caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')


