# pakiety w pythonie mają hierarchiczne nazwy
# ale nie są hierarchiczne (nie zawierają się jeden w drugim)

# from mathematica.geometry.figures import square_area
# def test_square_area():
#     assert square_area(5) == 25

# from mathematica.geometry import figures
# def test_square_area():
#     assert figures.square_area(5) == 25

# from mathematica.geometry import figures as f
# def test_square_area():
#     assert f.square_area(5) == 25

# nie zalecane - raczej nie używamy *, żeby nie wywoływać nieświadomie konfliktu nazw
# from mathematica.geometry.figures import *
from mathematica.geometry.figures import square_area, triangle_area, STALA


# mathematica.geometry - pakiet
# figures - moduł
# square_area, triangle_area - zawartość modułu (funkcje, klasy, stałe)
def test_square_area():
    assert square_area(5) == 25

def test_triangle_area():
    assert triangle_area(3,4) == 6

def test_stalej():
    assert STALA == 100