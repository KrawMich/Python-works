import random
opcje = ['k', 'p', 'n']

komp = 0
ty = 0
print('Gra kamien papier nozyce gramy do 2 wygranych')

while komp != 2 and ty != 2:
    wybor = input(f'Wprowadz wybór ? k/p/n :\n')
    if wybor not in opcje:
        print('Zły wybor')
        continue
    a = random.choice(opcje)
    print(a)
    if wybor == a:
        print('Remis nik nie dostaje punktu')
    elif (wybor == 'k' and a == 'p') or\
         (wybor == 'n' and a == 'p') or\
         (wybor == 'p' and a == 'k'):
        print('Pkt dla Ciebie')
        ty += 1
    else:
        komp += 1
        print('punkt dla komputera')
if komp == 2:
    print('Wygral komputer')
else:
    print('Wygrales')
