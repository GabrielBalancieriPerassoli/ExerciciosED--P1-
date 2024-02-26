def busca_elemento(vetor, x, n):
    if n == -1:
        return "Não achou"
    elif vetor[n] == x:
        return "Achou"
    else:
        return busca_elemento(vetor, x, n - 1)
    
vetor = [1,2,5,19]
x = 5
n = len(vetor) - 1    
print(busca_elemento(vetor, x, n))    