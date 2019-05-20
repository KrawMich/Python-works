# wyrazenie = input('Podaj wyrażenie : ')
# male = 0
# duze = 0
# liczby = 0
# pozostaleznaki = 0
#
# for i in wyrazenie:
#     if i.islower():
#         male += 1
#     elif i.isupper():
#         duze += 1
#     elif i.isdigit():
#         liczby += 1
#     else:
#         pozostaleznaki += 1
#
# print(f'Dużych liter jest : {duze}')
# print(f'Małych liter jest : {male}')
# print(f'Liczb jest : {liczby}')
# print(f'Pozostałych znaków jest : {pozostaleznaki}')

#drugi sposob z slownikiem dzieki czemu mozna pozniej latwiej to edytowac

wyrazenie = 'Ala ma 1 kota!'
ilosc_znakow = {
    'wielkie_litery' : 0,
    'male_litery' : 0,
    'cyfry' : 0,
    'pozostale_znaki' : 0
}
etykiety = {
    'wielkie_litery': 'Wielkie litery',
    'male_litery': 'Małe litery',
    'cyfry' : 'Cyfry',
    'pozostale_znaki' : 'Pozostałe znaki'
}
for i in wyrazenie:
    if i.islower():
        ilosc_znakow['male_litery'] += 1
    elif i.isupper():
        ilosc_znakow['wielkie_litery'] += 1
    elif i.isdigit():
        ilosc_znakow['cyfry'] += 1
    else:
        ilosc_znakow['pozostale_znaki'] += 1

for rodzaj, ilosc in ilosc_znakow.items():
    print(f'{etykiety[rodzaj]} : {ilosc}.')
