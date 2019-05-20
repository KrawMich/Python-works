import sys

uchwyt_do_pliku = open('dane.txt','w')
uchwyt_do_pliku.write('tralala')
uchwyt_do_pliku.close()

with open('dane.txt', 'w') as f:
    print('przed zapisem',f.closed)
    f.write('ala ma kota')
    print('po zapisie',f.closed)

print('po wyjsciu z with',f.closed)
#
# w - write - kasuje zawartość pliku, kursor na początku
# r - read - kursor jest na początku pliku
# a - append (write) - zawartość zostaje, kursor na koniec
# w+  - (read/write), kasuje zawartość, kursor na początku
# r+  - (read/write), zawartość zostaje, kursor na początku
# a+  - (read/write), zawartość zostaje, kursor na koniec
#
# wb, rb, ab, wb+, rb+, ab+  - odczyt/zapis bajtami, a nie znakami
print(sys.argv)