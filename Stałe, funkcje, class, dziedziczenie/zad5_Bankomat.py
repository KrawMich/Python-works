class CashMachine:
    MAX_CAPACITY = 100

    def __init__(self):
        self._case = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}

    def is_available(self) -> bool:
        # return bool(sum(self._case.values()))
        return sum(self._case.values()) > 0

    def put_money(self, banknotes: list):
        # banknotes = [100,'reklamówka',20,50,20, 'Kup pralkę']
        for paper in banknotes:
            if paper in self._case \
                    and sum(self._case.values()) < CashMachine.MAX_CAPACITY:
                self._case[paper] += 1
        # for nominal in self._case:
        #     self._case[nominal] +=...

    def withdraw_money(self, amount: int) -> list:
        # sposób 1:
        sorted_nominals = list(self._case.keys())
        sorted_nominals.sort(reverse=True)

        # sposób 2:
        sorted_nominals = sorted(self._case.keys(), reverse=True)

        do_wydania = []
        backup = self._case.copy()

        for nominal in sorted_nominals:
            ile_szt = min(amount // nominal, self._case[nominal])

            if ile_szt > 0:
                self._case[nominal] -= ile_szt
                do_wydania.extend([nominal] * ile_szt)
                amount -= nominal * ile_szt

        if amount == 0:
            return do_wydania
        else:
            self._case = backup
            return []

def test_availability():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()


def test_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()


def test_withdraw_money_from_empty():
    cash_machine = CashMachine()
    assert cash_machine.withdraw_money(150) == []


def test_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]


def test_withdraw_money_impossible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 50])
    assert cash_machine.withdraw_money(100) == []


def test_withdraw_money_2times_impossible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash_machine.withdraw_money(150)
    assert cash_machine.withdraw_money(150) == []


def test_withdraw_money_2times_possible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50, 50])
    cash_machine.withdraw_money(150)
    assert cash_machine.withdraw_money(150) == [100, 50]


def test_withdraw_money_all_banknotes():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(450) == [200, 100, 100, 50]


def test_withdraw_money_put_back_if_impossible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash_machine.withdraw_money(550)
    assert cash_machine.withdraw_money(450) == [200, 100, 100, 50]


# ten algorytm nie obejmuje przypadku z nominałami 20
# zadanie domowe z * - wymyślić lepszy algorytm
def test_withdraw_money_nominals():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50, 20, 20, 20])
    assert cash_machine.withdraw_money(160) == [100, 20, 20, 20]
