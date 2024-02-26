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

    node = No(valor)
    node.prox = linked_list 
    linked_list = node

    return linked_list 

def inicializa_lista(vetor):
    lista = None

    for i in reversed(vetor):
        lista = insere_inicio(lista, i)
    
    return lista

lista = inicializa_lista([1,2,3,4,5,6,7,8])

def lista_ligada_rec(P):
    if P != None:
        if P.prox != None:
            lista_ligada_rec(P.prox)
        print(P.info)

print(lista_ligada_rec(lista))
