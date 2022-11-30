code = []
answear = []
def binary(n):
    if n == 1:
        code.append(1)
        for i in reversed(code):
            answear.append(i)
        print(answear)

        #print(code)
    else:
        if n % 2 ==0:
            code.append(n % 2)
        elif n % 2 ==1:
            code.append(n % 2)
        n = n//2
        return binary(n)

binary(156)
