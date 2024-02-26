from Pilha import Pilha

# Implemente a função InicializaPilha(P) considerando uma
# pilha armazenada em lista ligada. Esta função deve
# inicializar a pilha devolvendo todas as células utilizadas
# para a memória

def InicializaPilha(P):

    while not P.PilhaVazia():

        Q = P

        P = P.prox 

        #dispose(Q)

    if P.PilhaVazia():

        P = None    


