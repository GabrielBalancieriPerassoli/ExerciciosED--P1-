from Fila import Fila

# Faça uma função que receba duas filas F1 e F2 ordenadas
# em ordem crescente e que gere uma única fila ordenada.
# As filas F1 e F2 ficarão vazias no processo

def OrdenaFila(F1, F2):
    F3 = Fila(tam + tam)

    while not F1.FilaVazia() and not F2.FilaVazia():

        if F1.PrimeiroDaFila() < F2.PrimeiroDaFila():

            x = F1.PrimeiroDaFila()
            F1.RemoveFila()

            F3.InsereFila(x)
        else:
            
            x = F2.PrimeiroDaFila()
            F2.RemoveFila()

            F3.InsereFila(x)

    # Adiciona os elementos restantes de F1, se houver
    while not F1.FilaVazia():

        x = F1.PrimeiroDaFila()
        F1.RemoveFila()

        F3.InsereFila(x)

    # Adiciona os elementos restantes de F2, se houver
    while not F2.FilaVazia():

        x = F2.PrimeiroDaFila()

        F2.RemoveFila()
        F3.InsereFila(x)

    lista_ordenada = []

    while not F3.FilaVazia():
        
        x = F3.PrimeiroDaFila()
        F3.RemoveFila()
        
        lista_ordenada.append(x)

    return lista_ordenada

tam = 4
F1 = Fila(tam)
F2 = Fila(tam)

F1.InsereFila(2)    
F1.InsereFila(5)
F1.InsereFila(20)
F1.InsereFila(50)

F2.InsereFila(1)
F2.InsereFila(8)
F2.InsereFila(10)
F2.InsereFila(48)

print(OrdenaFila(F1, F2))

