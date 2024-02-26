def CriarLista(TAM):
    vetor = [None] * TAM 
    return vetor

def JuntaLista(v1, v2, n1, n2):
    v3 = CriarLista(n1 + n2)

    for i in range(n1):
        v3[i] = v1[i]

    for j in range(n2):
        v3[n1 + j] = v2[j]    

    return v3

v1 = [1, 2, 3]
v2 = [4, 5, 6]
n1 = len(v1)
n2 = len(v2)
v3 = JuntaLista(v1, v2, n1, n2)
print("Lista combinada:", v3)  
