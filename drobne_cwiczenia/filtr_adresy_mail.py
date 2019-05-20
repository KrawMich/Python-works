import re

dane = [
    'test@test.pl',
    'Alamakota',
    'inny@firma.pl',
    'ksieradzki@alx.pl'
]

lista = []
for i in dane:
    if re.match('^[a-z0-9_.-]+@[a-z0-9_.-]+\.\w{2,4}$', i):
        lista.append(i)


print(lista)