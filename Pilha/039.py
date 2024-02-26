from Pilha import Pilha

def Posfixa(expressao):

    expressao = expressao.split() 

    P = Pilha(len(expressao) - 1)
    
    for token in expressao:

        if token.isdigit():
            P.Empilha(int(token))

        else:  
            op2 = P.Desempilha() 
            op1 = P.Desempilha()  
            if token == '+':
                P.Empilha(op1 + op2)
            elif token == '-':
                P.Empilha(op1 - op2)
            elif token == '*':
                P.Empilha(op1 * op2)
            elif token == '/':
                P.Empilha(op1 / op2)
    
    return P.Desempilha() 

expressao = "2 3 4 + + 3 7 * -"
resultado = Posfixa(expressao)
print("Resultado da expressão posfixa:", resultado)

