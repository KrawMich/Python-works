class Rownoleglobok():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole_powierzchni(self):
        raise NotImplementedError

class Prostokat(Rownoleglobok):
    def pole_powierzchni(self):
        return self.a * self.b

class Romb(Rownoleglobok):
    def __init__(self,a):
        super().__init__(a,a)

class Kwadrat(Prostokat,Romb):
    pass

k = Kwadrat(5)
print(k.pole_powierzchni())