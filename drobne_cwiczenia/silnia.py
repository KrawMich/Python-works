# def silnia(liczba):
#     silnia = 1
#     for liczby in range(1, liczba):
#         silnia += liczby * silnia
#     return silnia


def test_wartosc_silni():
    assert silnia(5) == 120
    assert silnia(7) == 5040
    assert silnia(3) == 6
    assert silnia(0) == 1
    assert silnia(1) == 1

def test_silnia_zera():
    assert silnia(0) == 1


def silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba - 1)