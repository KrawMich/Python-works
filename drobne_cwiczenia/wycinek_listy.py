lista = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10]
poczatek = int(input('Podaj poczatek zakresu : '))
koniec = int(input('Podaj koniec zakresu : ')) + 1
lista2 = []

for i in lista:
    if i >= poczatek and i < koniec:
        lista2.append(i)

print(lista2)