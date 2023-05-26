"""
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 10: 
    contador += 1
    if contador == 6:
        continue
    print(contador, end=' ')
    if contador == 9:
        break
print('Acabou')

