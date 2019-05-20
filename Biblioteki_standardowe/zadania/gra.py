# >>> Menu:
# ... stan [g]ry
# ... [w]ilk na łódkę lub z łódki
# ... [k]oza na łódkę lub z łódki
# ... [s]ałata na łódkę lub z łódki
# ... [l]ódka na przeciwny brzeg
# ... [e]xit

class Gra():
    def __init__(self):
        self.lodka = ''
        self.brzegi = [
            {'wilk', 'koza', 'sałata'},
            set()
        ]
        self.polozenie_lodki = 0
        self._menu()
        self._interface()

    def _menu(self):
        print(f'Menu:\n'
              f'... [m]enu'
              f'... stan [g]ry\n'
              f'... [w]ilk na łódkę lub z łódki\n'
              f'... [k]oza na łódkę lub z łódki\n'
              f'... [s]ałata na łódkę lub z łódki\n'
              f'... [l]ódka na przeciwny brzeg\n'
              f'... [e]xit')

    def _interface(self):
        while True:
            op = input('co chcesz zrobić? ')
            if op == 'm': self._menu()
            if op == 'g': self._stan_gry()
            if op == 'w': self._zaladunek_rozladunek('wilk')
            if op == 'k': self._zaladunek_rozladunek('koza')
            if op == 's': self._zaladunek_rozladunek('sałata')
            if op == 'l': self._przeplyn()
            if op == 'e': self._wyjdz()

    def _wyjdz(self):
        print('do widzenia')
        exit(0)

    def _przeplyn(self):
        # przeplyniecie na przeciwny brzeg
        self.polozenie_lodki = 1 - self.polozenie_lodki
        self._zaladunek_rozladunek(self.lodka)
        self._czy_wygrana()

    def _stan_gry(self):
        # wyświetlanie
        print(f'brzeg pierwszy: #{"#".join(self.brzegi[0])}#\n'
              f'brzeg drugi: #{"#".join(self.brzegi[1])}#\n'
              f'łódka: {self.lodka if self.lodka else "##"}, '
              f'{"drugi" if self.polozenie_lodki else "pierwszy"} brzeg')

    def _zaladunek_rozladunek(self, ladunek):
        if ladunek == self.lodka:
            self.brzegi[self.polozenie_lodki].add(ladunek)
            self.lodka = ''
        elif ladunek in self.brzegi[self.polozenie_lodki]:
            self.brzegi[self.polozenie_lodki].remove(ladunek)
            self.lodka = ladunek
        else:
            print(f'{ladunek} na przeciwnym brzegu')

    def _czy_wygrana(self):
        if self.brzegi[1] == {'wilk','koza','sałata'}:
            print('WYRAGRANA GRATULACJE')
            exit(0)
        przeciwny_brzeg = self.brzegi[1 - self.polozenie_lodki]
        if len({'wilk', 'koza'} & przeciwny_brzeg) == 2:
            print('wilk zeżarł kozę')
            print('BUUU LAMA, PRZEGRANA, TŁUMY PŁACZĄ')
            exit(0)
        if len({'koza', 'sałata'} & przeciwny_brzeg) == 2:
            print('koza zeżarła sałatę')
            print('BUUU LAMA, PRZEGRANA, TŁUMY PŁACZĄ')
            exit(0)


Gra()
