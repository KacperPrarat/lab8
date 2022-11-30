def fibonaci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)


print(fibonaci(10))