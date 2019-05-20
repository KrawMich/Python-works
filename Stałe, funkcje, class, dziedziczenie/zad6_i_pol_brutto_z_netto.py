# zrób klasę, która przechowuje informację o
# kwocie netto i stawce VAT
# a umie pokazać (i ewentualnie zmienić) kwotę brutto




class Invoice():
    def __init__(self, net, vat=0.23):
        self.net = net
        self.vat = vat

    @property
    def kwota_brutto(self):
        return round(self.net * (self.vat + 1),2)

    @kwota_brutto.setter
    def kwota_brutto(self,new_brutto):
        self.net = round(new_brutto / (1 + self.vat),2)

poz = Invoice(100, 0.07)
print(poz.kwota_brutto)
poz2 = Invoice(100)
print(poz2.kwota_brutto)
poz2.kwota_brutto = 1000
print(poz2.net, poz2.kwota_brutto)



