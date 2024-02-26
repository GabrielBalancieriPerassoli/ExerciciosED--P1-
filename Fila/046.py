from Pilha import Pilha
from Fila import Fila

# Faça uma função que inverta os elementos de uma fila
# utilizando uma pilha

def InverteFila(P, F):
    while not F.FilaVazia():
        x = F.PrimeiroDaFila()
        F.RemoveFila()
        P.Empilha(x)
    
    while not P.PilhaVazia():
        x = P.ElementoDoTopo()
        P.Desempilha()
        F.InsereFila(x)

    while not F.FilaVazia():
        x = F.PrimeiroDaFila()
        F.RemoveFila()
        print(x)    

tam = 5
P = Pilha(tam)
F = Fila(tam)

F.InsereFila(1)
F.InsereFila(5)
F.InsereFila(6)
F.InsereFila(3)
F.InsereFila(2)
print("1")
print("5")
print("6")
print("3")
print("2")
print("------")

InverteFila(P, F)