from zjazd3.zad5_Bankomat import CashMachine
from zjazd3.zad8_wyjatki import NoSpaceError, WrongAmountError, ImpossibleError


class PremiumCashMachine(CashMachine):

    def put_money(self, banknotes: list):
        banknotes = [x for x in banknotes if x in self._case]
        if sum(self._case.values()) + len(banknotes) > self.MAX_CAPACITY:
            raise NoSpaceError
        super().put_money(banknotes)

    def withdraw_money(self, amount: int):
        if amount % 10 != 0:
            raise WrongAmountError

        banknotes = super().withdraw_money(amount)

        if sum(banknotes) == amount:
            return banknotes

        raise ImpossibleError
