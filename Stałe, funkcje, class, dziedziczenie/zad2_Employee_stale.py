class Employee(object):
    # stałe klasowe
    WORK_DAY = 8
    OVERTIME_MUL = 2

    def __init__(self, fname, lname, rate):
        self.fname = fname
        self.lname = lname
        self.rate = rate
        self.salary = 0

    def register_time(self, hours):
        if hours > Employee.WORK_DAY:
            self.salary += Employee.WORK_DAY * self.rate \
                           + (hours - Employee.WORK_DAY) \
                           * Employee.OVERTIME_MUL * self.rate
        else:
            self.salary += hours * self.rate

    def pay_salary(self):
        tmp = self.salary
        self.salary = 0
        return tmp


def test_create():
    employee = Employee(fname='Jan', lname='Nowak', rate=100.0)
    assert True


def test_zarejestruj_zwykle_godziny():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500


def test_przychodzi_po_kase_dwa_razy():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.pay_salary()
    assert employee.pay_salary() == 0


def test_nadgodziny():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200


def test_dwa_dni_pracy():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    employee.register_time(5)
    assert employee.pay_salary() == 1700
