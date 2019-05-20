import re
dane = [
    '81-222',
    '00-212',
    'Ala',
    'Ma',
    '33-212'

]
lista = []
for i in dane:
    if re.match('^[0-9]{2}-[0-9]{3}$', i):
        lista.append(i)

print(lista)


