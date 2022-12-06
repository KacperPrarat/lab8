pierwsze = []
for liczba in range(2,100):
    czy_pierwsza = True
    for i in pierwsze:
        if liczba % i == 0:
            czy_pierwsza = False
    if czy_pierwsza:
        pierwsze.append(liczba)
def factorize(n):
    x = 0
    if n > 1:
        while n% pierwsze[x] != 0:
            x = x +1
        print(pierwsze[x])
        factorize((n/pierwsze[x]))


factorize(96)





