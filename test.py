towar = [{'nazwa':'banan','jednostka':'kg','ilosc':10,'cena':3},
{'nazwa':'jabłko','jednostka':'kg','ilosc':16,'cena':2.5},
{'nazwa':'mąka pszenna','jednostka':'op.','ilosc':30,'cena':2.5},
{'nazwa':'mydło','jednostka':'szt.','ilosc':6,'cena':1.5},
{'nazwa':'jogurt naturalny','jednostka':'szt.','ilosc':20,'cena':1.5},
{'nazwa':'papier toaletowy','jednostka':'op.','ilosc':10,'cena':9}]

def wyszukaj(towar,zapytanie):
    for slownik in towar:
        if zapytanie == slownik["nazwa"]:
            return slownik


def sumuj(towar,zapytanie):
    suma=0
    for slownik in towar:
        if zapytanie == slownik["nazwa"]:
            ilosc = slownik["ilosc"]
            cena = slownik["cena"]
            suma = ilosc * cena
    return suma


def sumujwszystko(towar):
    suma=0
    for slownik in towar:
            ilosc = slownik["ilosc"]
            cena = slownik["cena"]
            sumatmp = ilosc * cena
            suma = suma + sumatmp
    return suma

def dodajtowar(slownik,nazwa,jednostka,ilosc,cena):
    slownik.append({
    "nazwa" : nazwa,
    "jednostka": jednostka,
    "ilosc": ilosc,
    "cena": cena
    })
    return slownik



def ilosc(towar,rzecz,ilosc):
    for podslownik in towar:
        if podslownik["nazwa"] == rzecz:
            podslownik["ilosc"] = ilosc
        return towar

def filtr_jednostka(towar,jenostka):
    dict1 = []
    for podslownik in towar:
        if podslownik["jednostka"] == jenostka:
            dict1.append(podslownik)
    return dict1

print(filtr_jednostka(towar,"szt."))