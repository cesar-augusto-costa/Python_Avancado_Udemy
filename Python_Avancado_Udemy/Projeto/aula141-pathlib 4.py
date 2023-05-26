# YOUTUBE
# Manipulando caminhos, pastas e arquivos no Python com pathlib

from pathlib import Path

caminho_arquivo = Path(__file__)

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

caminho_arquivo.write_text('')

with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\r\n')
    file.write('Outra linha\r\n')

print(caminho_arquivo.read_text())
