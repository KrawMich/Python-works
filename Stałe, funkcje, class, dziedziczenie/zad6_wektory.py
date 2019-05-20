class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x},{self.y})'

    def __repr__(self):
        return str(self)

    # metoda obsługująca operator +
    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError

    # metoda obsługująca operator -
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # metoda obsługująca operator *
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    # metoda obsługująca funkcję abs
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    # less than <
    def __lt__(self, other):
        return abs(self) < abs(other)

    # grater than >
    def __gt__(self, other):
        return abs(self) > abs(other)

    # less equal <=
    def __le__(self, other):
        return abs(self) <= abs(other)

    # greater equal >=
    def __ge__(self, other):
        return abs(self) >= abs(other)

    # equal ==
    def __eq__(self, other):
        return abs(self) == abs(other)

    # not equal !=
    def __ne__(self, other):
        return abs(self) != abs(other)

# program
a = Vector(3, 4)
lista = [a, a, a]
print('a:', a)
print(lista)

b = Vector(-1, 2)
print('b:', b)
c = a + b
print('c:', c)

d = a - b
print('d:', d)

e = a * 4
print('e:', e)

# f = a + "ala ma kota"
# print('f:', f)

if a > b:
    print('a jest dłuższy')
else:
    print('a nie jest dłuższy')


# różne "zewnętrzne" funkcje
# del(a)
# len(a)

print(abs(a))

lista = [a,b,c,d,e]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)



