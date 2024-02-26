def SomaVetor(vetor, n):
    if n == -1:
        return 0
    else:
        return vetor[n - 1] + SomaVetor(vetor, n - 1)
    
vetor = [1,5,15,10,1]
n = len(vetor) - 1

print(SomaVetor(vetor, n))