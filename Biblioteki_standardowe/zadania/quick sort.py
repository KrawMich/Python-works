# Zadanie 2
# Zaimplementuj funkcję sort realizującą algorytm sortowania "quick sort". Funkcja powinna zwracać nową listę. Wraz z rozwiązaniem zaimplementuj także testy sprawdzające poprawność działania algorytmu.
#
# Przykład użycia funkcji:
#
# >>> sort([5, 1, 3, 2, 4])
# [1, 2, 3, 4, 5]

# 1. sprawdz czy masz co sortować
# 2. wybierz element podzialu
# 3. podziel liste na 3 kawalki : mniejsz, rowne, wieksze
# 4. posortuj mniejsze i wieksze (rekurencja)
# 5. scal mniejsze + rowne + wieksze i oddaj jako swoj wynik

def quick_sort(list_to_sort, krok=0):

    if len(list_to_sort) < 2:
        print(f'#{krok}:{list_to_sort} - nie ma czego sortować')
        return list_to_sort

    pivot = list_to_sort[0]
    minor,equal,major = [],[],[]

    for el in list_to_sort:
        if el < pivot:
            minor.append(el)
        elif el == pivot:
            equal.append(el)
        else:
            major.append(el)

    # 3x biegamy po liście (wolniej)
    # minor = [x for x in list_to_sort if x < pivot]
    # equal = [x for x in list_to_sort if x == pivot]
    # major = [x for x in list_to_sort if x > pivot]

    print(f'#{krok}:{list_to_sort}, '
          f'pivot:{pivot}, '
          f'#{krok+1}:{minor}, '
          f'#{krok+2}:{major}')

    minor = quick_sort(minor,krok+1)
    major = quick_sort(major,krok+2)

    print(f'#{krok} zbieram dane:',minor, major)

    return minor + equal + major

def test_z_przypadku_uzycia():
    assert quick_sort([5, 1, 3, 2, 4]) == [1, 2, 3, 4, 5]