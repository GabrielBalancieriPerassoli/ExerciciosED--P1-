
def LocalizaElem(vetor, n, i):
    
    if i < 0 or i > n:
        return "Problema de Indíce"
    else:
        print("No indíce", i)
        return vetor[i]
    
vetor = [1,2,3,4,5]
n = len(vetor) - 1
i = 3

print(LocalizaElem(vetor, n, i))