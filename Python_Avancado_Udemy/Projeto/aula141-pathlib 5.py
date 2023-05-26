# YOUTUBE
# Manipulando caminhos, pastas e arquivos no Python com pathlib

from pathlib import Path
from shutil import rmtree

caminho_pasta = Path.home() / 'Desktop' / 'Python_Legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

arquivo = subpasta / 'arquivo.txt'
arquivo.touch()
arquivo.write_text('Hey')

# caminho_pasta.rmdir()
# precisa apagar de dentro pra fora

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    # if file.is_file(): Se é arquivo
    # if file.is_dir(): Se é diretório
    
    # Se existir apaga, se não, cria
    if file.exists():
        file.unlink()
    else:
        file.touch()
    
    with file.open('a+') as text_file:
        text_file.write('Olá Mundo\n')
        text_file.write(f'file_{i}.txt')

# apaga tudo de uma vez
# rmtree(caminho_pasta)

def rmtree(root: Path, remove_root=True):
    # for file in root.glob('**/*.txt'):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            # file.rmdir()
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE:', file)
            file.unlink()
    
    if remove_root:
        root.rmdir()
        
rmtree(caminho_pasta)
