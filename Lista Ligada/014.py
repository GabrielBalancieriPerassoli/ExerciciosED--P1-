class No:
    def __init__(self, info):
        self.info = info
        self.prox = None

    def __str__(self):
        no = self
        lista_str = '['
        while no != None:
            lista_str += str(no.info)
            if no.prox:
                lista_str += ', '
            no = no.prox
        lista_str += ']'

        return lista_str

def insere_inicio(linked_list, valor):
    if linked_list == None:
        linked_list = No(valor)
        return linked_list
    
def inicializa_lista(vetor):
    lista = None

    for i in reversed(vetor):
        lista = insere_inicio(lista, i)
    
    return lista

lista = inicializa_lista([2,5,7,4,1])    

def par_antes(P):
    atual = P

    if P != None:
        if P.prox == None:
            return P 

    if P != None:
 
        while atual.prox != None:

            if P.prox.info % 2 == 0:
                Q = atual.prox
                atual.prox = atual.prox.prox
                P = insere_inicio(P, Q.info)
            else:
                atual = atual.prox

        return P
    
print(par_antes(lista))    