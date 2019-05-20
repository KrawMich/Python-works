print('jestem w module rownoleglobok')

from importowanie.czworokat import Czworokat

class Rownoleglobok(Czworokat):
    def __init__(self, a,b):
        self.a = a
        self.b = b