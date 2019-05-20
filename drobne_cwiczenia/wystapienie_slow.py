def liczenie_slow():
    wyrazenie = 'Ala ma kota a kot ma Ale'
    lista = wyrazenie.split()
    return print(dict([(x, lista.count(x)) for x in lista]))


liczenie_slow()
