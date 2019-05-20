class PremiumCashMachineError(Exception):
    pass

class NoSpaceError(PremiumCashMachineError):
    pass

class WrongAmountError(PremiumCashMachineError):
    pass

class ImpossibleError(PremiumCashMachineError):
    pass

# try:
#     raise ImpossibleError
# except PremiumCashMachineError:
#     print('złapany')