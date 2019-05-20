def test_lata_poprawne():
    assert lata_przystepne(1990,2002)== [1992, 1996, 2000]

def test_pusty_zakres():
    assert lata_przystepne(2002,2003) == []

def lata_przystepne(a,b):
    lista = []
    for lata in range(a,b+1):
        if lata % 4 == 0 and (lata % 100 != 0 or lata % 400 ==0):
            lista.append(lata)
    return lista
    # return lista(filter(lambda lata: lata % 4 == 0 and (lata % 100 != 0 or lata % 400 ==0),range (a, b+1))
#
# lata_przystepne(a = int(input('podaj poczatek zakresu : ')), b = int(input('Podaj konoec zakresu : ')))