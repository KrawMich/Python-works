from collections import defaultdict
from zjazd3.zad1_Product_tdd import Product


class Basket(object):

    def __init__(self):
        self.content = defaultdict(int)


    # ozdobniki, oznaczające, że metoda spodziewa się argumetów
    # typu Product i int
    def add_product(self, product:Product, pcs:int):
        # sposób 1:

        # if product in self.content:
        #     self.content[product] += pcs #dodaj do istniejących
        # else:
        #     self.content[product] = pcs #stwórz nowy wpis w słowniku

        # sposób 2:
        self.content[product] += pcs

    # ozdobnik, oznaczający, że metoda zwraca wynik typu float
    def count_total_price(self)->float:
        # sposób 1:

        # total_price = 0
        # for pr in self.content:
        #     pcs = self.content[pr]
        #     price = pr.price
        #     cost = pcs*price
        #     total_price += cost
        # return total_price

        # sposób 2:
        return sum([self.content[pr]*pr.price for pr in self.content])

def test_pusty_koszyk():
    basket = Basket()
    assert isinstance(basket, Basket)
    assert type(basket) == Basket


def test_kilka_tych_samych_produktow():
    basket = Basket()  # przygotowanie pustego koszyka
    product = Product(1, 'Woda', 10.00)  # tworzę produkt
    basket.add_product(product,5)  # wrzucam 5szt produktu do koszyka
    assert basket.count_total_price() == 50  # suma produktów w koszyku to 50


def test_dodaj_kilka_razy():
    basket = Basket()  # przygotowanie pustego koszyka
    product = Product(1, 'Woda', 10.00)

    basket.add_product(product, 1)
    basket.add_product(product, 5)
    basket.add_product(product, 2)

    assert basket.count_total_price() == 80


def test_kilka_produktow():
    basket = Basket()  # przygotowanie pustego koszyka
    product1 = Product(3, 'Wino', 5.00)
    product2 = Product(4, 'Woda', 10.00)

    basket.add_product(product1, 2)
    basket.add_product(product2, 5)

    assert basket.count_total_price() == 60

