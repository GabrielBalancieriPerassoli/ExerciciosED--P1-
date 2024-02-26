from Pilha import Pilha

# Implemente uma fila utilizando duas pilhas.
# • Deve ser proposta uma estrutura de dados TpFila que
# seja um registro onde as duas pilhas sejam campos da
# estrutura
# • Implemente as operações de manipulação desta fila

def Enfileirar(P1, x):
    P1.Empilha(x)

    print(x)

def Desenfileirar(P1, P2):

    while not P1.PilhaVazia():

        x = P1.ElementoDoTopo()
        P1.Desempilha()

        P2.Empilha(x)

    while not P2.PilhaVazia():

        x = P2.ElementoDoTopo()
        P2.Desempilha()

        print(x)

tam = 5
P1 = Pilha(tam)
P2 = Pilha(tam)        

Enfileirar(P1, 3)
Enfileirar(P1, 4)
Enfileirar(P1, 5)
Enfileirar(P1, 6)
Enfileirar(P1, 7)
print("-")
Desenfileirar(P1, P2)
Desenfileirar(P1, P2)
Desenfileirar(P1, P2)
Desenfileirar(P1, P2)
Desenfileirar(P1, P2)
