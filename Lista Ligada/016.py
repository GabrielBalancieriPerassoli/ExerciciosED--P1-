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

p1 = inicializa_lista([2,5,7,1])
p2 = inicializa_lista([1,4,5,6])

def TwoList(p1, p2):

    if p1 != None and p2 != None:
        Q = p1

        while Q.prox != None:
            Q = Q.prox

        if Q.prox == None:
            Q.prox = p2

    return p1      

print(TwoList(p1, p2))   
