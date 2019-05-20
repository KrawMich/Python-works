print('Potęgowanie')
podstawa = int(input('Podaj liczbę którą chcesz potęgować ?'))
wykladnik = int(input('Do której potęgi chcesz podnieść liczbę ?'))
x = 0
wynik = 1

while x != wykladnik:
        x += 1
        wynik = podstawa ** x

print(f' {podstawa} do potęgi {wykladnik} to {wynik}')

