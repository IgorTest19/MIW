from file_manager import FileManager

#Zad1

a_list = [0,1,2,3,4]
b_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def Zad1(a_list, b_list):
    c_list = []
    i = 0
    if len(a_list) > len(b_list):
        dlugosc = len(a_list)
    else:
        dlugosc = len(b_list)
    while i < dlugosc:
        if i < len(a_list) and i % 2 == 0:
            c_list.append(i)
        if i < len(b_list) and i % 2 != 0:
            c_list.append(i)
        i += 1
    return c_list
print(Zad1(a_list,b_list))



#Zad2

def zad2(data_text):
    length = len(data_text)
    letters = list(data_text)
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    return {
        "length: ": length,
        "letters: ": letters,
        "big_letters: ": big_letters,
        "small_letters: ": small_letters
            }

print(Zad2("Metody Inżynierii Wiedzy"))


#Zad3
def zad3(text, letter):
    return text.replace(letter, '')

print(Zad3("Metody Inżynierii Wiedzy", 'i'))


def zad3(text, letter):
    slowo = [i for i in text if i != letter.upper() and i != letter.lower()]
    return ''.join(slowo)

print(Zad3("Metody Inżynierii Wiedzy", 'i'))


#Zad4

def zamiana_stopni(temperature_type):
    if temperature_type < -273.15:
        zamiana = "Zimniej się nie da!"
    else:
        fahrenheit = temperature_type * 1.8 + 32
        rankine = (temperature_type + 273.15) * 1.8
        kelvin = temperature_type + 273.15
        zamiana = "{0:.2f} stopni Celsjusza to {1:.2f} Fahreheita, {2:.2f} Rankine i {3:.2f} Kelvina".format(temperature_type, fahrenheit, rankine, kelvin)
    return zamiana

print(zamiana_stopni(-273.15))


#Zad5

class Calculator:
    """
    Klasa kalkulator posiadająca funkcje:

    add - dodawania

    difference - odejmowania

    multiply - mnożenia

    divide - odejmowania
    """

    def __init__(self, liczba_1, liczba_2):
        self.liczba_1 = liczba_1
        self.liczba_2  = liczba_2

    def add(self):
        return self.liczba_1 + self.liczba_2

    def difference(self):
        return self.liczba_1 - self.liczba_2

    def multiply(self):
        return self.liczba_1 * self.liczba_2

    def divide(self):
        if self.liczba_2 != 0:
            wynik = self.liczba_1 / self.liczba_2
        else:
            wynik = "Podzielono przez zero... (╯ ͠° ͟ʖ ͡°)╯┻━┻"
        return wynik

# kalkulator = Calculator(1,0)
# print(kalkulator.add())
# print(kalkulator.difference())
# print(kalkulator.multiply())
# print(kalkulator.divide())




#Zad6

class ScienceCalculator(Calculator):
    """
    Klasa kalkulator naukowy z dodatkowymi funkcjami:

    powers - potęgowanie liczby pierwszej
    do potęgi liczby drugiej

    root - pierwiastek liczby pierwszej
    stopnia liczby drugiej
    """

    # def powers(self):
    #     for x in range(1, self.liczba_2):
    #         self.liczba_1 *= self.liczba_1
    #     return self.liczba_1

    def powers(self):
        return self.liczba_1**self.liczba_2

    def root(self):
        return self.liczba_1**(1/self.liczba_2)


# sc = ScienceCalculator(2,3)
# print(ScienceCalculator.__doc__)
# print(sc.add())
# print(sc.powers())
# sc2 = ScienceCalculator(8,3)
# print(sc2.root())


#Zad7

def reverse(tekst):
    """
    Funkcja wypisująca podany tekst od tyłu
    :param tekst: zmienna typu string
    :return: zmienna typu string
    """
    return tekst[::-1]

print(reverse("koteł"))


#Zad8/9

fm = FileManager("test.txt")
fm.read_file()
fm.update_file("Nowy tekst")


#Zad10


