def fibi(n):
    if n > 0:
        if n == 1:
            return 1
        elif n == 2:
            print('1')
            return 1
        else:
            a = 1
            b = 1
            for i in range(2, n + 1):
                prox = a + b
                a = b
                print(a) 
                b = prox
            return b    

print(fibi(4))                