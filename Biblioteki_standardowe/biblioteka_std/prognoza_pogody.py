import json
import urllib.request

URL_SEARCH = 'https://www.metaweather.com/api/location/search/?query='
URL_LOCATION = 'https://www.metaweather.com/api/location/'


# with urllib.request.urlopen('http://pywaw.org/') as url:
#     dane = url.read()
#     print(dane)

loc_name = input('Podaj nazwę lokalizacji: ')
with urllib.request.urlopen(URL_SEARCH + loc_name) as url:
    dane = url.read()

# json.load(plik)
# json.loads(napis)
struktura = json.loads(dane) #uwaga na 's' na końcu!
# print(struktura)
if len(struktura) == 0:
    print('nieznana lokalizacja')
    exit(0)
if len(struktura) == 1:
    woeid = struktura[0]['woeid']
if len(struktura) > 1:
    print('Wybierz lokalizację: ')
    for i,loc in enumerate(struktura):
        print(f'[{i}] : {loc["title"]}')
    i = int(input('\n'))
    woeid = struktura[i]['woeid']

# print(woeid)
with urllib.request.urlopen(URL_LOCATION + str(woeid)) as url:
    dane = url.read()

struktura = json.loads(dane)
# print(struktura)
prognoza_na_dzis = struktura['consolidated_weather'][0]
print('Prognoza na dziś:')
print('temp min',prognoza_na_dzis['min_temp'])
print('temp max',prognoza_na_dzis['max_temp'])
print('wilgotność',prognoza_na_dzis['humidity'])
print('ciśnienie',prognoza_na_dzis['air_pressure'])
print('kierunek wiatru',prognoza_na_dzis['wind_direction_compass'])
#
# prognoza na dziś:
# temp_min
# temp_max
# kierunek wiatru
# cisnienie
# wilgotnosc