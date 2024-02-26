from Pilha import Pilha
from Fila import Fila

# • Implemente uma pilha utilizando duas filas.
# • Deve ser proposta uma estrutura de dados TpPilha que
# seja um registro onde as duas filas sejam campos da
# estrutura
# • Implemente as operações de manipulação desta pilha

tam = 3
f1 = Fila(tam)
f2 = Fila(tam)

def Empilhar2(f1, x):
    f1.InsereFila(x)
    return x

def Desempilhar2(f1, f2):

    if f2.FilaVazia():

        while not f1.FilaVazia():

            x = f1.RemoveFila()
            f2.InsereFila(x)

    if not f2.FilaVazia():

        topo_pilha = None

        while not f2.FilaVazia():

            x = f2.RemoveFila()
            if f2.FilaVazia():
                topo_pilha = x
            else:
                f1.InsereFila(x)

        return topo_pilha
    else:

        print("Pilha vazia")      

print(Empilhar2(f1, 1))      
print(Empilhar2(f1, 2))
print(Empilhar2(f1, 3))  
print("-")
print(Desempilhar2(f1, f2))
print(Desempilhar2(f1, f2))
print(Desempilhar2(f1, f2))