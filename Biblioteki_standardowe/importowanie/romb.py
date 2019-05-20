print('jestem w module romb')

from importowanie.czworokat import Czworokat
from importowanie.rownoleglobok import Rownoleglobok

class Romb(Rownoleglobok):
    def __init__(self, a):
        super().__init__(a,a)

print('jestem programem', __name__)
c = Czworokat()
figura = Romb(6)