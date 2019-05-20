class Product:

    def __init__(self, id, name, price):
        self.ob_id = id
        self.ob_name = name
        self.ob_price = price

    def print_info(self):
        print(f'Produkt "{self.ob_name}", '
              f'id:{self.ob_id}, '
              f'cena:#{self.ob_price:.2f}#PLN')


p1 = Product(1,'Woda',10.99)
p1.print_info()

p2 = Product(2,"Sok",4.50)
p2.print_info()
