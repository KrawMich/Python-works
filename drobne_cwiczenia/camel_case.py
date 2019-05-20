def to_camel_case(wyrazenie):
    gotowy = ''
    zamien_na_wielka = True
    for znak in wyrazenie:
        if znak.isalpha() or znak.isdigit():
            gotowy += znak.upper() if zamien_na_wielka else znak

        zamien_na_wielka = znak.isspace()

    return gotowy


def test_puste_wyrazenie():
    assert to_camel_case('') == ''


def test_usun_znaki_specjalne():
    assert to_camel_case('Python!') == 'Python'


def test_zamien_na_camel_case():
    assert to_camel_case('Litwo, ojczyzno moja!') == 'LitwoOjczyznoMoja'


"""
kwota = 100
do_rabatu = 50

rabat = 0.05 if kwota > 100 else 0

if kwota > 100:
    rabat = 0.05
else:
    rabat = 0
    
TAK W PYTHONIE SIĘ NIE DA :    kwota > 100 ? 0.05 : 0;
"""