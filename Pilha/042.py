from Pilha import Pilha
from Fila import Fila

# Faça uma função que inverta os elementos de uma pilha utilizando uma fila

tam = 4

P = Pilha(tam) 
F = Fila(tam)

P.Empilha(4)
P.Empilha(3)
P.Empilha(1)
P.Empilha(2)
P.Empilha(8)

def InverterPilha(P):

    while not P.PilhaVazia():

        x = P.ElementoDoTopo()
        P.Desempilha()

        if not F.FilaCheia():

            F.InsereFila(x)

    while not F.FilaVazia():

        x = F.PrimeiroDaFila()
        F.RemoveFila()

        if not P.PilhaCheia():

            P.Empilha(x)

    return P

print(InverterPilha(P))                
