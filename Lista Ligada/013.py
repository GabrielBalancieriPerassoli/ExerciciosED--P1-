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

def remove_negativo(P):

    if P != None:
        ant = None 
        atual = P 

        while atual != None:
            if atual.info < 0:
                if ant == None:
                    P = atual.prox
                else:
                    ant.prox = atual.prox

                prox = atual.prox
                #dispose(atual)
                #atual = prox
            else:
                ant = atual
                atual = atual.prox
