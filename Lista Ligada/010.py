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

def invera_lig_esvazia(P):
    if P != None:
        LI = None;
        while (P != None):
            # novo(Q)
            # Q.info = P.info
            # Q.prox = LI
            # LI = Q
            # R = P
            P = P.prox
            # dispose(R);