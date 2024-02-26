
def CombinarListas(P1,P2):

    P3 = None

    if (P1 != None) and (P2 != None):

        P3 = P1

        while(P1.prox != None):
            P1 = P1.prox

        if (P1.prox == None):
            P1.prox = P2
            P1 = None
            P2 = None    