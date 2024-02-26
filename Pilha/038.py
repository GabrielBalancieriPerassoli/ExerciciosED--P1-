from Pilha import Pilha

def Parentrizacao(P, expressao):

    for c in expressao:
        if c == "(":
            P.Empilha(c)
        elif c == "[":
            P.Empilha(c)
        elif c == "{":
            P.Empilha(c)
        elif c == ")":
            if P.PilhaVazia() or P.ElementoDoTopo() != "(":
                return False
            P.Desempilha()
        elif c == "]":
            if P.PilhaVazia() or P.ElementoDoTopo() != "[":
                return False
            P.Desempilha()
        elif c == "}":
            if P.PilhaVazia() or P.ElementoDoTopo() != "{":
                return False
            P.Desempilha()
            
    if P.PilhaVazia():
        return True
    else:
        return False

expressao = "4 + [2 * 8]"
tamanho = len(expressao)
P = Pilha(tamanho)
print(Parentrizacao(P, expressao))   
