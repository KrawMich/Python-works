print('jestem w module czworokat')
print('jestem importowanym modulem', __name__)

class Czworokat():
    print('przed initem czworokata')
    a = 8
    def __init__(self):
        pass
    print('po inicie czworokata')

print('po definicji klasy czworokat')

