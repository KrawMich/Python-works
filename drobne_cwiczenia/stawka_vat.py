dane = (200 ,300, 400)
wyplata = 0
vat = float(input('Podaj stawke VATu : '))

for i in dane:
        wyplata += (i - 15) * (1 - vat)

print(wyplata)