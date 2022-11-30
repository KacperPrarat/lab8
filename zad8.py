def binarna(liczba):
    kodbinarny = []
    if (liczba/2) ==0:
        print(kodbinarny)
    else:
       x = liczba % 2
       if x == 0:
           kodbinarny.append(0)
       if x == 1:
            kodbinarny.append(1)
       liczba = (liczba/2)
       binarna(liczba)

print(binarna(156))


