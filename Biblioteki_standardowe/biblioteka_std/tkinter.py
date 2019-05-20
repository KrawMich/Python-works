import tkinter
from tkinter import ttk,messagebox


def policz():
    try:
        cena = float(cena_entry.get())
        spalanie = float(spalanie_entry.get())
        dystans = float(dystans_entry.get())
        koszt = dystans * cena * spalanie / 100
        koszt_label.configure(text=str(koszt))
    except:
        # koszt_label.configure(text='podaj wartości liczbowe')
        messagebox.showerror('błąd','podaj wartości liczbowe')


root = tkinter.Tk()
root.title('okienko')

# cena paliwa
cena_label = tkinter.Label(master=root, text='Cena paliwa')
cena_entry = tkinter.Entry(master=root)

cena_label.grid(row=1, column=1)
cena_entry.grid(row=1, column=2)

# spalanie
spalanie_label = tkinter.Label(master=root, text='Spalanie l/100km')
spalanie_entry = tkinter.Entry(master=root)

spalanie_label.grid(row=3, column=1)
spalanie_entry.grid(row=3, column=2)

# dystans
dystans_label = tkinter.Label(master=root, text='Dystans km')
dystans_entry = tkinter.Entry(master=root)

dystans_label.grid(row=5, column=1)
dystans_entry.grid(row=5, column=2)

# spacja = tkinter.Label(master=root, text=' ')
# spacja.grid(row=2,column=3,columnspan=2)
# spacja.grid(row=4,column=3,columnspan=2)


koszt_label = tkinter.Label(master=root, text='-- policz --')
koszt_label.grid(row=6,column=1,columnspan=2)

guzik = tkinter.Button(master=root, text='policz', command=policz)
guzik.grid(row=7,column=1,columnspan=2)

comboExample = ttk.Combobox(master=root,
                            values=["January",
                                    "February",
                                    "March",
                                    "April"])
comboExample.grid(row=8,column=1,columnspan=2)

root.mainloop()

# py2exe
