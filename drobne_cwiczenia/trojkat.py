print('Trójkąt')

bok1 = int(input('Podaj długość pierwszego boku : '))
bok2 = int(input('Podaj długość drugiego boku : '))
bok3 = int(input('Podaj długość trzeciego boku : '))

if bok1 >= bok2 and bok1 >= bok3 :
    najdluzszy = bok1
    min1 = bok2
    min2 = bok3

elif bok2 >= bok1 and bok2 >= bok3 :
    najdluzszy = bok2
    min1 = bok1
    min2 = bok3

elif bok3 >= bok1 and bok3 >= bok2 :
    najdluzszy = bok3
    min1 = bok1
    min2 = bok2

if najdluzszy >= min1 + min2 :
    print('To nie jest trójkąt')
elif najdluzszy**2 == min1**2 + min2**2 :
    print('Jest to trójkąt prostokątny')
elif najdluzszy**2 > min1 ** 2 + min2 ** 2 :
    print('Jest to trójkąt rozwartokątny ')
elif min1 == min2 or min1 == najdluzszy or min2 == najdluzszy :
    print('Jest to trójkąt równoramienny')
# elif najdluzszy ** 2 < min1 ** 2 + min2 ** 2 :
#     print('Jest to trójkąt rozwarto kątny')