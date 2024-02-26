def elevado(x, n):
    if n == 0 or x == 1:
        return 1
    elif n == 1:
        return x
    elif n > 0:
        return x * elevado(x, n - 1)
    else:
        return 1 / elevado(x, -n)
    
print(elevado(1, 5))