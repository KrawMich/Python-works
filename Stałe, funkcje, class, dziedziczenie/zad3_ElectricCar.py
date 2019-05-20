class ElectricCar(object):
    # stała klasowa
    RANGE_FACTORY = 1.0

    def __init__(self, max_range):
        self.max_range = max_range
        self.battery_level = max_range * ElectricCar.RANGE_FACTORY

    def drive(self, planned_range):
        # self.battery_level -= ile_przejechał_tak_naprawde

        # if planned_range > self.battery_level:
        #     tmp = self.battery_level
        #     self.battery_level = 0
        #     return tmp
        # else:
        #     self.battery_level -= planned_range
        #     return planned_range

        real_dist = min(planned_range, self.battery_level)
        self.battery_level -= real_dist
        return real_dist


    def charge(self):
        self.battery_level = self.max_range


def test_zasieg_samochodu():
    bmw = ElectricCar(100)  # maksymalny zasięg
    assert bmw.drive(100) == 100


def test_poza_zasiegiem():
    tesla = ElectricCar(30)
    assert tesla.drive(50) == 30


def test_ladowanie():
    car = ElectricCar(100)
    car.drive(70)
    car.charge()  # ładujemy zawsze do końca
    assert car.drive(90) == 90


def test_2_trasy():
    car = ElectricCar(100)
    car.drive(70)
    car.drive(20)
    assert car.drive(50) == 10
