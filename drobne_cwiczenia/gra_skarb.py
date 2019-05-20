from random import randint

skarb_x = randint(1, 10)
skarb_y = randint(1, 10)
gracz_x = randint(1, 10)
gracz_y = randint(1, 10)
ilosc_ruchow = 0
potrzebna_ilosc_ruchow = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

print(f'Skarb jest na pozycji {skarb_x}, {skarb_y}.')
print(f'Użytkownik jest na pozycji {gracz_x}, {gracz_y}.')

while True:
    ilosc_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    print('W - góra, A - lewo, S - dół, D - prawo ')
    ruch = input('Dokąd zmierzasz?.. ')
    ruch = ruch.lower()
    ilosc_ruchow += 1

    if ruch == 'w':
        gracz_y += 1
    elif ruch == 'a':
        gracz_x -= 1
    elif ruch == 's':
        gracz_y -= 1
    elif ruch == 'd':
        gracz_x += 1

    ilosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    print('')
    print(f'Użytkownik jest na pozycji {gracz_x}, {gracz_y}.')

    if skarb_x == gracz_x and skarb_y == gracz_y:
        print(f'Brawo! Skarb jest Twój! Potrzebowałeś/aś {ilosc_ruchow} ruchów.')
        break

    if  gracz_x <= 0  or gracz_x > 10 or gracz_y <= 0 or gracz_y > 10:
        print('Spadasz w przepaść. To koniec poszukiwań.')
        break

    if randint(1, 5) != 5:
        if ilosc_po_ruchu < ilosc_przed_ruchem:
            print('*' * 50)
            print('Ciepło.. skarb coraz bliżej..')
            print('*' * 50)
        else:
            print('*' * 50)
            print('Zimno.. skarb oddala się..')
            print('*' * 50)

    if ilosc_ruchow >= potrzebna_ilosc_ruchow * 2 :
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        potrzebna_ilosc_ruchow = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        ilosc_ruchow = 0
        print('Koniec i bomba, kto nie zdążył ten trąba. Skarb uciekł.')
