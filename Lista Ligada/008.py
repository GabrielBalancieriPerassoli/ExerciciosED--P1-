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
    
def inversa_ligada(P):
    if P != None:

        ant = None 
        atual = P 
        prox = None 
        
        while (atual != None):
            prox = atual.prox 
            atual.prox = ant
            ant = atual 
            atual = prox

        return ant    

print(inversa_ligada([1,2,3,4,5,6,7,8]))              

