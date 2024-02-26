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
    novo_no = No(valor)
    novo_no.prox = linked_list
    return novo_no
    
def insere_final(linked_list, valor):
    if linked_list == None:
        return No(valor)

    node = linked_list 
    while node.prox != None:
        node = node.prox
    node.prox = No(valor)

    return linked_list    
    
def inicializa_lista(vetor):
    lista = None

    for i in reversed(vetor):
        lista = insere_inicio(lista, i)
    
    return lista

p1 = inicializa_lista([2,5,7,8])
p2 = inicializa_lista([1,4,3,6])

def MesclarListasOrdenadas(p1, p2):
    p3 = None

    while (p1 != None) and (p2 != None):
        if p1.info < p2.info:
            p3 = insere_final(p3, p1.info)
            p1 = p1.prox
        else:
            p3 = insere_final(p3, p2.info)
            p2 = p2.prox

    while p1 != None:
        p3 = insere_final(p3, p1.info)
        p1 = p1.prox

    while p2 != None:
        p3 = insere_final(p3, p2.info)
        p2 = p2.prox

    return p3        

print(MesclarListasOrdenadas(p1, p2))
