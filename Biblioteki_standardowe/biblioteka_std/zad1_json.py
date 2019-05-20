import json


class Pracownik():
    _STALA = 'bardzo tajne dane'

    def __init__(self,imie,nazwisko,email, rok,pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.rok = rok
        self.pensja = pensja

    def __str__(self):
        return self.imie + ' ' + self.nazwisko
    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {'imie':self.imie,
                'nazwisko':self.nazwisko,
                'email':self.email,
                'rok':self.rok,
                'pensja':self.pensja}

    # dygresja:

    # @staticmethod
    # def modelowy_pracownik():
    #     return Pracownik('Ania','Kowalska','a@a.pl',2000,3000)
    #
    # @classmethod
    # def dostep_do_wspolnej_przestrzeni(cls):
    #     return cls._STALA

    @staticmethod
    def from_dic(dane):
        return Pracownik(dane['imie'],
                         dane['nazwisko'],
                         dane['email'],
                         dane['rok'],
                         dane['pensja'])

DATABASE_FILE_NAME = 'pracownicy.json'

if __name__ == '__main__':

    try:
        with open(DATABASE_FILE_NAME,'r') as f:
            baza_z_json = json.load(f)
            # print(baza_z_json)
            baza = [Pracownik.from_dic(slownik) for slownik in baza_z_json]
            # print(baza)
    except FileNotFoundError:
        baza = []

    while True:
        operacja = input('co chcesz zrobić? '
                         '[w - wypisz, d - dodaj, u - usuń, z - zakończ]')
        operacja = operacja.lower()

        if operacja in 'wu':
            for i, prac in enumerate(baza,start=1):
                print(f'[{i}] {prac}')

        if operacja == 'u':
            nr = int(input('którego usunąć (podaj nr): '))
            del(baza[nr-1])

        if operacja == 'd':
            imie = input('imie: ')
            nazwisko = input('nazwisko: ')
            email = input('email: ')
            rok = int(input('rok urodzenia: '))
            pensja = float(input('pensja: '))

            prac = Pracownik(imie,nazwisko,email,rok,pensja)
            baza.append(prac)

        if operacja == 'z':
            with open(DATABASE_FILE_NAME,'w') as f:
                baza_dla_json = [prac.to_dict() for prac in baza]
                json.dump(baza_dla_json,f)

            break

