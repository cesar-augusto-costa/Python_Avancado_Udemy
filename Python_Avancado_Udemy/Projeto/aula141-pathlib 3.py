# YOUTUBE
# Manipulando caminhos, pastas e arquivos no Python com pathlib

from pathlib import Path

print(Path.home() / 'Desktop')
arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch() # cria o arquivo
print(arquivo)
arquivo.write_text('Olá mundo')
print(arquivo.read_text())
arquivo.unlink() # apaga o arquivo


