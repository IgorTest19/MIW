

#ZAD 1

zmienna_string = """Lorem Ipsum jest tekstem stosowanym jako przykładowy
wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w.
przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć
wieków później zaczął być używany przemyśle elektronicznym, pozostając
praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz
z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum,
a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem
przeznaczonym do realizacji druków na komputerach osobistych,
jak Aldus PageMaker"""


#ZAD 2

imie = "Igor"
nazwisko = "Ciuciura"

litera_1 = imie[2]
litera_2 = nazwisko[3]

liter_1_ilosc = imie.count(litera_1)
litera_2_ilosc = nazwisko.count(litera_2)

print("W tekście jest {0} liter {1} oraz {2} liter {3}"
      .format(liter_1_ilosc, litera_1, litera_2_ilosc, litera_2)
      )


#ZAD 3

##1

print("{:>20}".format("Witaj!"))


##2

print("{:_<20}".format("Świecie!"))

##3

print("{:^20}".format("Python"))

##4

slownik = {'pierwszy': 'Python', 'drugi': '3.7'}

print("{pierwszy} {drugi}".format(**slownik))

##5

print("{:=+5d} {}".format(100, "do pancerza"))


#ZAD 4

zmienna_typu_string = "Wyrazy testowe"

print(dir(zmienna_typu_string))

help(zmienna_typu_string.isprintable)

print(zmienna_typu_string.isprintable())


#ZAD 5

student = "Igor Ciuciura"

print((student[::-1]).capitalize())


#ZAD 6

lista_oryginalna = list(range(1, 11))

lista_nowa1 = lista_oryginalna[5:]

lista_oryginalna = lista_oryginalna[:5]

print(lista_oryginalna)

print(lista_nowa1)


#ZAD 7

lista_oryginalna = list(range(1, 11))

lista_nowa1 = lista_oryginalna[5:]

lista_oryginalna = lista_oryginalna[:5]

index = 0

element = 0

lista_oryginalna.insert(index, element)

kopia_listy = (lista_oryginalna + lista_nowa1).copy()

print(kopia_listy)

kopia_listy.sort(reverse = True)

print(kopia_listy)


#ZAD 8

lista_stud = ((156091, "Adam Kowalski"), (1593685, "Jonasz Braders"))


#ZAD 9

lista_stud2 = {
    156091 : {
    'imie': "Adam",
    'nazwisko': "Kowalski",
    'wiek': 25,
    'e-mail': "adam.kowalski@gmail.com",
    'rok urodzenia': 1995,
    'adress': "80-298 Gdańsk, Juliusza Słowackiego 21,"
    },
    159385: {
        'imie': "Jonasz",
        'nazwisko': "Braders",
        'wiek': 29,
        'e-mail': "jonasz.braders@gmail.com",
        'rok urodzenia': 1991,
        'adress': "00-693 Warszawa, Marszałkowska 89,"
    }

}

#ZAD 10

numery_tel = ["600 500 400", "600 500 400", "960 560 560", "690 800 800", "690 800 800"]

print(set(numery_tel))


#ZAD 11

for x in range(1,11):
    print(x)


#ZAD 12

for x in range(100, 15, -5):
    print(x)


#ZAD 13

lista_aut = [
    {
        "marka": "Audi",
        "model": "A7",
        "cena": 150000,
        "pojemność": 3.0,
        "kolor": "biały"
    },
    {
        "marka": "Lexus",
        "model": "GS",
        "cena": 180000,
        "pojemność": 4.0,
        "kolor": "srebrny"
    },
    {
        "marka": "Volvo",
        "model": "S90",
        "cena": 165000,
        "pojemność": 2.0,
        "kolor": "brązowy"
    }
]

for auto in lista_aut:
    print (
        "Na sprzedaż mamy {0} samochód {1} {2} z silnikiem o pojemności {3}."
        " {1} kosztuje tylko {4} złotych ".format(auto["kolor"], auto["marka"],
        auto["model"], auto["pojemność"], str(auto["cena"]))
    )
