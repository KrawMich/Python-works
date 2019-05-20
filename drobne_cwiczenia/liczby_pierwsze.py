from math import sqrt

min = int(input('Podaj warotosc minimalna : '))
max = int(input('Podaj warotsc maksymalna : '))
ile_liczb = 0
for liczba in range(min, max + 1):
    jest_Pierwsza = True

    for dzielnik in range(2, int(sqrt(liczba))+1):
        if liczba % dzielnik == 0:
            jest_Pierwsza = False
            break

    # jezeli znajdzie dzielnik to liczba nie jest pierwsza jesli znajdzie to jest pierwsza
    if jest_Pierwsza:
        ile_liczb += 1
        print(f'liczba {liczba} jest pierwsza')
    if ( ile_liczb != 0 and ile_liczb % 100 == 0 ):
        pytanie = input('Czy jechac dalej t/n : ')
        if pytanie != 't':
            ile_liczb += 1
            quit ()
        else:
            print(f'Liczba {liczba} nie jest pierwsza')
