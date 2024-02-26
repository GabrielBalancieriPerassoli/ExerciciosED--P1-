

# • Implemente a função InicializaFila(Q) considerando uma
# fila armazenada em lista ligada. Esta função deve
# inicializar a fila devolvendo todas as células utilizadas
# para a memória

# I            # F
# 3 -> 4 -> 1 -> 2

def InicializaFila(Q):

    while Q.Inicio != None:

        R = Q.Inicio 
        Q.Inicio = Q.Inicio.prox 
        #dispose(R) 

    Q.Fim = None     
        