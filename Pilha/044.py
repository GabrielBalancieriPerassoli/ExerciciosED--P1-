from Pilha import Pilha
import random

# • Faça uma função que implemente duas pilhas em um
# único vetor

def CriarLista(TAM):
    vetor = [None] * TAM 

    return vetor

def InserirElem(vetor, n, valor, i, TAM):
    if i < 0 or i > TAM:
        return "Problema de Índice"
    elif n < TAM:
        for j in range(n, i, -1):
            vetor[j + 1] = vetor[j]
    
    vetor[i] = valor 
    n = n + 1

    return vetor

def Tamanho(vetor):
    return len(vetor)

vetor = CriarLista(8)
print(vetor)

def TwoPilhasVetor(vetor):

    tam = Tamanho(vetor) - 1

    if tam % 2 == 0:

        tam1 = tam // 2
        tam2 = tam // 2 
        
    else:
        tam1 = tam // 2
        tam2 = (tam // 2) + 1

    P1 = Pilha(tam1)
    P2 = Pilha(tam2)

    while not P1.PilhaCheia() and not P2.PilhaCheia():
        x = random.randint(1, 50) 
        x2 = random.randint(1, 50)

        P1.Empilha(x)
        P2.Empilha(x2)

    print(P1) 
    print(P2)    

    i = 0

    while not P1.PilhaVazia():
        x = P1.ElementoDoTopo()
        P1.Desempilha()
        InserirElem(vetor, -1, x, i, tam)
        i += 1

    while not P2.PilhaVazia():
        x = P2.ElementoDoTopo()
        P2.Desempilha()
        InserirElem(vetor, -1, x, i, tam)
        i += 1   

    return vetor    

print(TwoPilhasVetor(vetor))        
