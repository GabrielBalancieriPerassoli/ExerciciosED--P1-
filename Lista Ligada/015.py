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

lista = inicializa_lista([5,5,1,4,1])  

def repetido(P):

    if P == None or P.prox == None:
        return False
    else:

        atual = P

        while atual != None:

            comparar = P.prox

            while comparar != atual:

                if atual.info == comparar.info:
                    return True 
                
                comparar = comparar.prox

            atual = atual.prox

        return False    
    
print(repetido(lista))    
