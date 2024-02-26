def fibr(n):
    if n > 0:
        if n == 1:
            return 1
        else:
            return fibr(n - 1) + fibr(n - 2)
        
print(fibr(11))            