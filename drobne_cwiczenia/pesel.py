def czy_poprawny_pesel(pesel):
    mnozniki = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    kontrolna = sum([waga * int(cyfra) for waga, cyfra in zip(mnozniki, pesel)])
    return str(kontrolna)[-1] == '0'


def test_czy_poprawny_pesel():
    assert czy_poprawny_pesel(pesel='80072909146')
    assert czy_poprawny_pesel(pesel='92071314764')


def test_czy_bledny_pesel():
    assert not czy_poprawny_pesel(pesel='80072903146')


# w3c  www consorcium
# i18n internationalization
# l10n localization