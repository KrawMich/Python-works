from zjazd3.zad8_PremiumCashMachine import PremiumCashMachine
from zjazd3.zad8_wyjatki import PremiumCashMachineError

cm = PremiumCashMachine()
cm.MAX_CAPACITY = 5
try:
    cm.put_money([20,50,100,'ala ma kota', 'kup pralkę', 500])
    print(cm.withdraw_money(150))
except PremiumCashMachineError as err:
    print('nie da się')
finally:
    print('dziękujemy za skorzystanie z naszych usług')


