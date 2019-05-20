
import json
import urllib.request
import tkinter
from tkinter import ttk, messagebox

URL_CURRENCY = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=json'


def policz_kupno():
    try:
        cena = float(cenawaluty[lista_walut_combobox.get()])
        ilosc = float(ilosc_waluty_entry.get())
        wynik = round(ilosc/cena, 2)
        otrzymasz_label.configure(text=f'Otrzymasz {str(wynik)} {lista_walut_combobox.get()}')
    except:
        messagebox.showerror('błąd', 'podaj wartości liczbowe')


def policz_sprzedaz():
    try:
        cena = float(cenawaluty[lista_walut_combobox.get()])
        ilosc = float(ilosc_waluty_entry.get())
        wynik = round(ilosc * cena, 2)
        otrzymasz_label.configure(text=f'Otrzymasz {str(wynik)} PLN')
    except:
        messagebox.showerror('błąd','podaj wartości liczbowe')

def sprzedaz():
    ilosc_waluty_label.configure(text="Ile waluty chcesz sprzedać")
    policz_button.configure(text='Sprzedaż', command=policz_sprzedaz)


def kupno():
    ilosc_waluty_label.configure(text="Ile PLN chcesz wymienić")
    policz_button.configure(text='Kupno', command=policz_kupno)


def ceny():
    messagebox.showinfo(title="Ceny", message=listacen)


root = tkinter.Tk()
root.title('Kursy walut')

menu = tkinter.Menu(root)
root.config(menu=menu)
sub_menu = tkinter.Menu(menu)
sub_menu1 = tkinter.Menu(menu)
menu.add_cascade(label="Plik", menu=sub_menu)
menu.add_cascade(label="Aktualne ceny", menu=sub_menu1)
sub_menu1.add_cascade(label="Wyświetl", command=ceny)
sub_menu.add_command(label="kupno", command=kupno)
sub_menu.add_command(label="sprzedaż", command=sprzedaz)
sub_menu.add_separator()
sub_menu.add_command(label="Zamknij", command=quit)

with urllib.request.urlopen(URL_CURRENCY) as url:
    dane = url.read()
struktura = json.loads(dane)
struktura1 = struktura[0]["rates"]

listawalut = []
listacen = []

for i in struktura1:
    listawalut.append(f'{i["code"]}  {i["currency"]}')
    x = f'{i["code"]} {i["mid"]} \n'
    listacen.append(x)


cenawaluty = {}

for i, struk in enumerate(struktura1):
    cenawaluty[listawalut[i]] = struk["mid"]

wybor_waluty_label = tkinter.Label(master=root, text='Wybierz walute')
wybor_waluty_label.grid(row=2, column=1)

lista_walut_combobox = ttk.Combobox(master=root,
                                    values=listawalut)
lista_walut_combobox.current(0)
lista_walut_combobox.grid(row=2, column=2, columnspan=4)

dzien_kursow = struktura[0]["effectiveDate"]
kursy_na_dzien_label = tkinter.Label(master=root, text=f'Kurs na dzień - {dzien_kursow} ')
kursy_na_dzien_label.grid(row=1, column=1, columnspan=3)

ilosc_waluty_label = tkinter.Label(master=root, text='Ile złotych chcesz wymienić ?')
ilosc_waluty_label.grid(row=3, column=1, columnspan=2)

ilosc_waluty_entry = tkinter.Entry(master=root, bg="yellow")
ilosc_waluty_entry.grid(row=3, column=4)

policz_button = tkinter.Button(master=root, text='Kupno', command=policz_kupno, fg="purple")
policz_button.grid(row=4, columnspan=5)

otrzymasz_label = tkinter.Label(master=root, text='--policz--', fg="red")
otrzymasz_label.grid(row=5, columnspan=5)

photo = tkinter.PhotoImage(file="male.png")
photo_lebel = tkinter.Label(master=root, image=photo)
photo_lebel.grid(row=6, column=2)


root.mainloop()
