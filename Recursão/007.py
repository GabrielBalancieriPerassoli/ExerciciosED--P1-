def maior_vetor(vetor, n):
    if n == - 1:
        return "Vazia"
    elif n == 0:
        return vetor[0]
    else:
        if vetor[n] > maior_vetor(vetor, n - 1):
            return vetor[n]
        else:
            return maior_vetor(vetor, n - 1)
        
vetor = [1,20,19,5]
n = len(vetor) - 1
print(maior_vetor(vetor, n))          