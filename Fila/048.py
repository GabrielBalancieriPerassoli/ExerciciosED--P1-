from Fila import Fila

# Faça uma função que receba uma fila de números
# inteiros e que devolva a mesma fila com todos os
# elementos positivos posicionados antes de todos os
# elementos negativos

def CriarLista(TAM):
    vetor = [None] * TAM
    return vetor

def PosAntDoNeg(F):

    tam_fila = 6  # Obtendo o tamanho real da fila
    v1 = CriarLista(tam_fila)   # Criando vetores com tamanho adequado
    v2 = CriarLista(tam_fila)

    i1 = 0  # Índice para v1
    i2 = 0  # Índice para v2

    while not F.FilaVazia():
        x = F.PrimeiroDaFila()

        if x < 0:
            v2[i2] = x
            i2 += 1
        else:
            v1[i1] = x
            i1 += 1

        F.RemoveFila()

    # Reinserindo os elementos na fila com a ordem desejada
    for j in range(i1):
        F.InsereFila(v1[j])

    for j in range(i2):
        F.InsereFila(v2[j])

    # Imprimindo os elementos da fila após a modificação
    while not F.FilaVazia():
        print(F.PrimeiroDaFila())
        F.RemoveFila()
    

tam = 6
F = Fila(tam)

F.InsereFila(-5)
F.InsereFila(-4)
F.InsereFila(4)
F.InsereFila(-1)
F.InsereFila(3)
F.InsereFila(-2)

print(PosAntDoNeg(F))