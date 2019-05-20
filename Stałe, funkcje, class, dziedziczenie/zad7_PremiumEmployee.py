from zjazd3.zad2_Employee_stale import Employee


class PremiumEmployee(Employee):
    def __init__(self, fname, lname, rate):
        super().__init__(fname, lname, rate)
        self._bonus = 0

    def give_bonus(self, premia):
        self._bonus += premia

    def pay_salary(self):
        za_godziny = super().pay_salary()
        za_premie = self._bonus
        self._bonus = 0
        return za_godziny + za_premie

def test_premii():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500

def test_premii_jednorazowa():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000)
    employee.pay_salary()
    assert employee.pay_salary() == 0

def test_premii_dwa_razy():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 2500

def test_create():
    employee = PremiumEmployee(fname='Jan', lname='Nowak', rate=100.0)
    assert True


def test_zarejestruj_zwykle_godziny():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500


def test_przychodzi_po_kase_dwa_razy():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.pay_salary()
    assert employee.pay_salary() == 0


def test_nadgodziny():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200


def test_dwa_dni_pracy():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    employee.register_time(5)
    assert employee.pay_salary() == 1700