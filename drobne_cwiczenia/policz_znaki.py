

def policz_znaki(zdanie, start ='<', koniec='>'):
    zliczanie = 0
    waga = 0
    for znak in zdanie:
        if znak == start:
            waga += 1
        elif znak == koniec:
            waga -= 1
        else:
            zliczanie += waga
    return zliczanie



def test_liczenie_znakow():
    assert policz_znaki('ala ma <kota> a <kot >ma ale') == 8
    assert policz_znaki('miasto <gdansk jest> nad morzem') == 11
    assert policz_znaki('ala [ma kota kot] ma ale' , '[',']') == 11
    assert policz_znaki('ala ma k<o<t<a>>> kot ma ale') == 6