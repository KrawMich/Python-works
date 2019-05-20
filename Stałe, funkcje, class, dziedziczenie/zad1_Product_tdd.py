class Product(object):
    def __init__(self, id, name, price):
        self.price = price
        self.name = name
        self.id = id

    def print_info(self):
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN'


# Test Driven Development
# GIVEN - przygotowanie środowiska
# WHEN - wywołanie testowanej funkcjonalności
# THEN - sprawdzenie efektów czy zgodne z oczekiwanymi

def test_create():
    pr = Product(id=1,name='Woda',price=10.99)
    assert pr.id == 1
    assert pr.name == 'Woda'
    assert pr.price == 10.99


def test_info():
    pr = Product(1, 'Woda', 10.99)
    assert pr.print_info() == 'Produkt "Woda", id: 1, cena: 10.99 PLN'


def test_info2():
    pr = Product(15, 'Sok', 12)
    assert pr.print_info() == 'Produkt "Sok", id: 15, cena: 12.00 PLN'

