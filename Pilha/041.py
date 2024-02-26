from Pilha import Pilha

# Faça uma função que receba uma pilha e que remova um
# elemento que se encontre na base da estrutura.
# • (dica: utilize uma pilha auxiliar na solução proposta)

tamanho = 4

P = Pilha(tamanho)
P2 = Pilha(tamanho)

P.Empilha(3)
P.Empilha(10)
P.Empilha(1)
P.Empilha(5)
P.Empilha(8)

def Base(P):

    while not P.PilhaVazia():

        x = P.ElementoDoTopo()
        P.Desempilha()

        if not P2.PilhaCheia():

            P2.Empilha(x)

    if P2.PilhaCheia():

        x = P2.ElementoDoTopo()
        P2.Desempilha()

    return P2 

P2 = Base(P)

print("P2 após remover a base de P:", P2)



