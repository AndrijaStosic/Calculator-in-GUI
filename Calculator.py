from tkinter import *

prozor = Tk()
prozor.title("Calculator")
prozor.config(bg="black")
prozor.geometry("300x400")

dal_puta = 0
dal_plus = 0
dal_minus = 0
dal_podeljeno = 0

lista_brojeva = []
trenutni_broj = ""

def azuriraj_ekran(text):
    ekran.config(text=text)

def dodaj_cifru(cifra):
    global trenutni_broj
    trenutni_broj += str(cifra)
    azuriraj_ekran(trenutni_broj)

def klik_nula():
    dodaj_cifru(0)

def klik_jedan():
    dodaj_cifru(1)

def klik_dva():
    dodaj_cifru(2)

def klik_tri():
    dodaj_cifru(3)

def klik_cetiri():
    dodaj_cifru(4)

def klik_pet():
    dodaj_cifru(5)

def klik_sest():
    dodaj_cifru(6)

def klik_sedam():
    dodaj_cifru(7)

def klik_osam():
    dodaj_cifru(8)

def klik_devet():
    dodaj_cifru(9)

def set_operacija(operacija):
    global dal_puta, dal_plus, dal_minus, dal_podeljeno, trenutni_broj

    if trenutni_broj != "":
        lista_brojeva.append(int(trenutni_broj))
        trenutni_broj = ""
    
    if operacija == "+":
        dal_plus = 1
    elif operacija == "-":
        dal_minus = 1
    elif operacija == "*":
        dal_puta = 1
    elif operacija == "/":
        dal_podeljeno = 1

def dali_plus():
    set_operacija("+")

def dali_minus():
    set_operacija("-")

def dali_puta():
    set_operacija("*")

def dali_podeljeno():
    set_operacija("/")

def racunaj():
    global dal_puta, dal_plus, dal_minus, dal_podeljeno, trenutni_broj

    if trenutni_broj != "":
        lista_brojeva.append(int(trenutni_broj))
        trenutni_broj = ""

    if len(lista_brojeva) < 2:
        return

    prvi_broj = lista_brojeva.pop(0)
    drugi_broj = lista_brojeva.pop(0)
    
    rezultat = 0
    if dal_puta == 1:
        rezultat = prvi_broj * drugi_broj
        dal_puta = 0
    elif dal_minus == 1:
        rezultat = prvi_broj - drugi_broj
        dal_minus = 0
    elif dal_plus == 1:
        rezultat = prvi_broj + drugi_broj
        dal_plus = 0
    elif dal_podeljeno == 1:
        rezultat = prvi_broj / drugi_broj
        dal_podeljeno = 0

    azuriraj_ekran(rezultat)
    lista_brojeva.append(rezultat)

def CE():
    global trenutni_broj, lista_brojeva, dal_puta, dal_plus, dal_minus, dal_podeljeno
    trenutni_broj = ""
    lista_brojeva = []
    dal_puta = dal_plus = dal_minus = dal_podeljeno = 0
    azuriraj_ekran(0)

ekran = Label(prozor, text="0", height=2, bg="white", anchor="e", font=("Arial", 24))
ekran.pack(fill="both")

nula = Button(prozor, text="          0             ", height=2, bg="lightblue", fg="Red", command=klik_nula)
nula.place(x=50, y=300)

zarez = Button(prozor, text="    .    ", height=2, bg="lightblue", fg="Red")
zarez.place(x=150, y=300)

jednako = Button(prozor, text="    =    ", height=6, bg="Lightgreen", fg="Black", command=racunaj)
jednako.place(x=200, y=250)

jedan = Button(prozor, text="    1    ", height=2, bg="lightblue", fg="Red", command=klik_jedan)
jedan.place(x=50, y=250)

dva = Button(prozor, text="    2    ", bg="lightblue", fg="Red", height=2, command=klik_dva)
dva.place(x=100, y=250)

tri = Button(prozor, text="    3    ", bg="lightblue", fg="Red", height=2, command=klik_tri)
tri.place(x=150, y=250)

cetiri = Button(prozor, text="    4    ", height=2, fg="Red", bg="lightblue", command=klik_cetiri)
cetiri.place(x=50, y=200)

pet = Button(prozor, text="    5    ", height=2, bg="lightblue", fg="Red", command=klik_pet)
pet.place(x=100, y=200)

sest = Button(prozor, text="    6    ", height=2, bg="lightblue", fg="Red", command=klik_sest)
sest.place(x=150, y=200)

plus = Button(prozor, text="    +    ", height=2, bg="silver", fg="Black", command=dali_plus)
plus.place(x=200, y=200)

sedam = Button(prozor, text="    7    ", height=2, bg="lightblue", fg="Red", command=klik_sedam)
sedam.place(x=50, y=150)

osam = Button(prozor, text="    8    ", height=2, bg="lightblue", fg="Red", command=klik_osam)
osam.place(x=100, y=150)

devet = Button(prozor, text="    9    ", height=2, bg="lightblue", fg="Red", command=klik_devet)
devet.place(x=150, y=150)

minus = Button(prozor, text="    -    ", height=2, bg="silver", fg="Black", command=dali_minus)
minus.place(x=200, y=150)

puta = Button(prozor, text="    *    ", height=2, bg="silver", fg="Black", command=dali_puta)
puta.place(x=200, y=100)

podeljeno = Button(prozor, text="    /    ", height=2, bg="silver", fg="Black", command=dali_podeljeno)
podeljeno.place(x=150, y=100)

obrisi = Button(prozor, text="    Clear(CE)    ", height=2, bg="gold", fg="Black", command=CE)
obrisi.place(x=50, y=100)

prozor.mainloop()
