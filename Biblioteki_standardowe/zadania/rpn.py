# 1 + 4 * 3 / 5 + 12 =
# 1 4 3 * 5 / + 12 +
# * / + + 1 4 3 5 12
#
# Zadanie 1
# Zaimplementuj funkcję rpn realizującą obliczenia wyrażenia w odwrotnej notacji polskiej. Funkcja powinna przyjmować zmienną liczbę argumentów. Wraz z rozwiązaniem zaimplementuj także testy sprawdzające poprawność działania funkcji.
#
# Przykład użycia funkcji:
#
# >>> rpn(2, 3, '+', 5, '*')
# 25
# Filmik: https://www.youtube.com/watch?v=7ha78yWRDlE


def rpn(*args):
    operators = {
        '+':lambda a,b: a+b,
        '-':lambda a,b: a-b,
        '*':lambda a,b: a*b,
        '/':lambda a,b: a/b,
    }
    stack = []
    for el in args:
        if type(el) in (int, float):
            stack.append(el)
        elif el in operators:
            arg1 = stack.pop()
            arg2 = stack.pop()
            ret = operators[el](arg2,arg1)
            stack.append(ret)
        else:
            raise ValueError

    if len(stack) == 1:
        return stack[0]

    raise ValueError

def test_dodawanie():
    assert rpn(12,13.5,'+') == 25.5
    
def test_dzielenie():
    assert rpn(12, 4, '/') == 3

def test_z_przypadku_uzycia():
    assert rpn(2, 3, '+', 5, '*') == 25