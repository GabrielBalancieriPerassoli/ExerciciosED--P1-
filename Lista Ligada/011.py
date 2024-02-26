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

def InsereOrdenado(linked_list, valor):
    if linked_list == None:
        return insere_inicio(linked_list, valor)
    elif linked_list.info > valor:
        return insere_inicio(linked_list, valor)
    else:
        atual = linked_list 

        while atual.prox != None and atual.prox.info < valor:
            atual = atual.prox
        
        node = No(valor)
        node.prox = atual.prox
        atual.prox = node
        
        return linked_list 

lista = inicializa_lista([1,2,20,4,14,6,7,8])    

def ordena_lista(P):
    if P == None:
        return 0 
    elif P != None:
        if P.prox == None:
            return P
    else:
        ordenada = None

        while P.prox != None:
            InsereOrdenado(ordenada, P.info)
            P = P.prox

        P = ordenada 
        ordenada = None  
        return P

print(ordena_lista(lista))              