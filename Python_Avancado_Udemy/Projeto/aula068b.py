"""
Escopo de funções em Python
Escopo significa o local onde aquele códico pode atingir.
Existe o escopo global e local.
O escopo GLOBAL é o escopo onde todo o código é alcançavel.
O escopo LOCAL é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1

def escopo():
    global x
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
