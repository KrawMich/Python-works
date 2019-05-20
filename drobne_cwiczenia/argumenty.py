# * łapie wszystkie argumenty nienazwane
def suma(*argumenty):
    print(argumenty)

suma(4, 5, 6)
suma(2, 2)
suma(8, 9, 10, 11)

# 88 łapie wszystkie argumenty nazwane
def zapisz(**informacje):
    print(informacje)

zapisz(imie = 'Jan', nazwisko = 'Nowak')
zapisz(wiek = 13)

# args - arguments
# kwargs - keyword arguments

def funkcja(*args, **kwargs):
    print(args)
    print(kwargs)

funkcja(13, 11, rok = 2000)