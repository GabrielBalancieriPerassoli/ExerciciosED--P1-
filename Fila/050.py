from Fila import Fila

# Faça uma função que receba uma fila de números
# inteiros e que esvazie esta lista da seguinte forma:
# • remova o primeiro elemento
# • se o número removido for positivo, decremente o número e o
# insira novamente na fila
# • Se o número removido for negativo ou zero, descarte este
# número

def FilaNumeros(F):

    while not F.PilhaVazia():

        if F.PrimeiroDaFila() > 0:

            x = F.PrimeiroDaFila() - 1
            F.RemoveFila()

            F.InsereFila(x)

        else:

            x = F.PrimeiroDaFila()
            F.RemoveFila()

    return F        

tam = 5
F = Fila(tam)

F.InsereFila(2)
F.InsereFila(-1)
F.InsereFila(5)
F.InsereFila(7)
F.InsereFila(-5)

print(FilaNumeros(F))



