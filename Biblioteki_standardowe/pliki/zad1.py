# python zad1.py ala.txt
import sys

# sprawdzenie czy jestem programem
if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        with open(file_name, 'r', encoding='UTF-8') as f:
            for i, line in enumerate(f.readlines(), start=1):
                print(i, line, end='')
    except IndexError:
        exit('podaj nazwę pliku')
    except FileNotFoundError:
        exit('plik o podanej nazwie nie istnieje')


