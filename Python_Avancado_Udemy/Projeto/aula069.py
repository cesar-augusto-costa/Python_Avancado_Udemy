"""
Escopo de funções em Python
Escopo significa o local onde aquele códico pode atingir.
Existe o escopo global e local.
O escopo GLOBAL é o escopo onde todo o código é alcançavel.
O escopo LOCAL é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palabra global faz uma variável do escopo externo ser a mesma 
no escopo interno.
USAR GLOBAL É UMA MÁ PRÁTICA, TEM QUE USAR PARAMETROS.
"""
x = 1

def escopo(): 
    # global x
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
