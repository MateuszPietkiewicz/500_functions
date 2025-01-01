# Cześć masz napisać jak najwięcej fukncji(500). Powodzenia :) każdy closure i decorator liczony razy 3

#1
def square_area(x):
    return x * x

assert square_area(2) == 4
assert square_area(3) == 9
assert square_area(5) == 25

#2
def ekstrakalasa_win(club):
    return f"Najlepszym klubem w polsce jest {club}"

assert ekstrakalasa_win("Jagiellonia") == "Najlepszym klubem w polsce jest Jagiellonia"

#3
def rectangle_area(x,y):
    return x * y

assert rectangle_area(2,4) == 8
assert rectangle_area(5,4) == 20
assert rectangle_area(3,5) == 15

#4, 5, 6

def power_n(exponent):
    def inner(base):
        return base ** exponent

    return inner

power_3 = power_n(3)
power_5 = power_n(5)

assert power_5(2) == 32
assert power_3(2) == 8

#7,8,9

def color_eyes(color):
    def inner(name):
        return f'{name} has {color} eyes.'
    return inner

zielone = color_eyes("green")
niebieskie = color_eyes("blue")


zielone("Ola")
niebieskie("Mateusz")

assert zielone("Ola") == "Ola has green eyes."
assert niebieskie("Mateusz") == "Mateusz has blue eyes."

#10, 11, 12
def person_height(wzrost):
    def inner(name):
        return f"{name} has {str(wzrost)} cm height."
    return inner

tall164 = person_height("164")
tall184 = person_height(184)
tall164("Ola")
tall184("Konstanty")

assert tall164("Ola") == "Ola has 164 cm height."
assert tall184("Konstanty") == "Konstanty has 184 cm height."

#13, 14, 15
def dzielisentencje(x):
    def inner(name):
        return name.split(x)

    return inner

spacja = dzielisentencje(' ')
przecinek = dzielisentencje(',')

s = spacja("Ala zrobiła co chciała, spoko?")
p = przecinek("Ala zrobiła co chciała, spoko?")

assert spacja("Ala zrobiła co chciała, spoko?") == ['Ala', 'zrobiła', 'co', 'chciała,', 'spoko?']
assert przecinek("Ala zrobiła co chciała, spoko?") == ['Ala zrobiła co chciała', ' spoko?']

#16
def _title(sentence):
    return sentence.title()

assert _title("kasia zrobiła co musiała.") == "Kasia Zrobiła Co Musiała."
assert _title("Basia zrobiła co musiała.") == "Basia Zrobiła Co Musiała."

#17, 18, 19 (20,21,22)
def _lower(fun):
    def inner(name):
        return fun(name.lower())

    return inner
@_lower
def siema(nazwa):
    return f"{nazwa} siema"

assert siema("BASIA") == "basia siema"
assert siema("SeBa") == "seba siema"

#23 ,24, 25(26, 27,28)
def _upper(funkcja):
    def inner(nazwa):
        return  funkcja(nazwa.upper())

    return inner

@_upper
def nara(nazwa):
    return f"{nazwa} nara"

assert nara("ukry") == "UKRY nara"
assert nara("hamburgery") == "HAMBURGERY nara"

#29, 30, 31
def _filter(min_v, max_v):
    def inner(value):
        return min_v < value <max_v
    return inner

filtr3_8 = _filter(3,8)
filtr2_20 = _filter(2,20)

assert filtr3_8(5) == True
assert filtr2_20(1) == False

#32, 33, 34 (35,36,37)

def _split(funkcja):
    def inner(name):
        return funkcja(name.split())
    return inner

@_split
def mnozymy2(dane):
    return dane * 2
assert mnozymy2("2 3 4") == ['2', '3', '4', '2', '3', '4']
assert mnozymy2("5 6 7") == ['5', '6', '7','5', '6', '7']

#38, 39, 40 (41, 42, 43)
def _find(funkcja):
    def inner(nm, x):
        return funkcja((nm).find(x))
    return inner

@_find
def name_is_here(x):
    if x == -1:
        return f"Nie znalazles {x}"
    return f'Znalazłes na indexie {x}'

assert name_is_here("Czy Kasia jest tutaj", "Kasia") == "Znalazłes na indexie 4"
assert name_is_here("Czy Kasia jest tutaj", "Basia") == "Nie znalazles -1"

#44, 45, 46 (47, 48, 49, 50 ,51, 52)

def swap(funkcja):
    def inner(name: str):
        return  funkcja(name.swapcase())

    return inner

@swap
def multiply2(x):
    return x * 2

assert multiply2("AsIa") == "aSiAaSiA"
assert multiply2("MateuSZ") == "mATEUszmATEUsz"

@swap
def multiply3(x):
    return x * 3

assert multiply3("Jan") == "jANjANjAN"
assert multiply3("Masza") == "mASZAmASZAmASZA"

#53, 54, 55, 56, 57 ,58 (59, 60, 61, 62, 63, 64)
def _tytul_(funckja):
    def inner(x):
        return funckja(x.title())
    return inner

def _podzial_(funckja):
    def inner(x):
        return funckja(x.split())
    return inner


@_tytul_
@_podzial_
def name_company(x: str):
    return f'{x[0]} {x[1]} sp. z o.o.'

assert name_company("geo pabieda") == "Geo Pabieda sp. z o.o."
assert name_company("pabieda iT") == "Pabieda It sp. z o.o."

@_tytul_
@_podzial_
def name_and_surname(x: str):
    return f"Imię: {x[0]} Nazwisko: {x[1]}"

assert name_and_surname("mati pietkiewicz") == "Imię: Mati Nazwisko: Pietkiewicz"
assert name_and_surname("aleksandra szymborska") == "Imię: Aleksandra Nazwisko: Szymborska"

#65

def metraz(x: int, y: int):
    return f"{x * y} m2 mieszkania."

assert metraz(3, 4)  == "12 m2 mieszkania."
assert metraz(5, 8)  == "40 m2 mieszkania."

#66, 67, 68 (69, 70, 71)

def how_many_rooms(fun):
    def inner(b):
        z = fun(b * 5)
        return  f"{z} m2 mieszkania"

    return inner

@how_many_rooms
def all_house(b):
    return b

assert all_house(5) == "25 m2 mieszkania"
assert all_house(10) == "50 m2 mieszkania"

#72,73,74 (75,76,77)
def size_room(funkcja):
    def inner(dlugosc, szerokosc):
        funkcja(dlugosc, szerokosc)
        pow = dlugosc * szerokosc
        return  f"Powierzchnia pokoju wynosi {pow} m2."
    return inner

@size_room
def wymiar(dlugosc, szerokosc):
    return f"Wymiary:{dlugosc} x {szerokosc}"

assert wymiar(5,4) == "Powierzchnia pokoju wynosi 20 m2."
assert wymiar(6,5) == "Powierzchnia pokoju wynosi 30 m2."


#78,79,80
def zew(x):
    def wew(y):
        return  x + y
    return wew

dodaj_10 = zew(10)
assert dodaj_10(20) == 30
assert dodaj_10(50) == 60

#81,82,83(84,85,86)
def zew2(fun):
    def wew2(x,y):
        fun(x,y)
        return  f"Wynik: {x + y}"
    return wew2

@zew2
def dodawanie(x,y):
    return x, y

assert dodawanie(5,5) == "Wynik: 10"
assert dodawanie(7,8) == "Wynik: 15"

#87, 88, 89 (90,91,92)
def zew3(fun):
    def wew3(x,y):
        fun(x,y)
        return  f"Wynik: {x - y}"
    return wew3

@zew3
def odejmowanie(x,y):
    return x, y

assert odejmowanie(5,5) == "Wynik: 0"
assert odejmowanie(7,8) == "Wynik: -1"

#93,94,95 (96,97,98)
def zew4(fun):
    def wew4(x,y):
        fun(x,y)
        return  f"Wynik: {x * y}"
    return wew4

@zew4
def mnoz(x,y):
    return x, y

assert mnoz(5,5) == "Wynik: 25"
assert mnoz(7,8) == "Wynik: 56"

#99, 100, 101 (102,103, 103)
def zew5(fun):
    def wew5(x,y):
        fun(x,y)
        return  f"Wynik: {x / y}"
    return wew5

@zew5
def dzielenie(x,y):
    return x, y

assert dzielenie(5,5) == "Wynik: 1.0"
assert dzielenie(4,8) == "Wynik: 0.5"

#104,105,106(107,108,109)
def zeww(fun):
    def inner(*args):
        fun(args)
        kk =[]
        for n in args:
            nn= n + 273.15
            kk.append(nn)
        return  kk
    return inner

@zeww
def kalwiny(*args):
    return f"{args} stopni Celsjusza"

assert kalwiny(0,1) == [273.15, 274.15]
assert kalwiny(8,9 ,100) == [281.15, 282.15, 373.15]

#110
def add10(*args):
    return [x + 10 for x in args]

assert add10(0,10,20) == [10, 20, 30]
assert add10(-10,110) == [0, 120]

#111
import datetime
week= {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
def tomorrow():
    cd = datetime.datetime.now()
    next_day = cd.isoweekday() + 1
    if next_day == 8:
        next_day = 1
    return week[next_day]

assert tomorrow() == week[(datetime.datetime.now().isoweekday() + 1)]

#112,113,114(115,116,117)
def tomorrow_c(func):
    def inner(day = None):
        if day is None:
            cd = datetime.datetime.now()
            tow = cd + datetime.timedelta(days=1)
            naz = func(tow.strftime("%A"))
            return naz
        next_day = day + 1 if day < 7 else 1
        return func(week[next_day])
    return inner

@tomorrow_c
def jutro(day):
    return f"Jutro taki dzień: {day}"

assert jutro() == f"Jutro taki dzień: {week[(datetime.datetime.now().isoweekday() + 1)]}"
assert jutro(4) == "Jutro taki dzień: Friday"
assert jutro(7) == "Jutro taki dzień: Monday"

#118
import datetime
week= {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

def yesterday():
    y_day = datetime.datetime.now() - datetime.timedelta(days=1)
    day = y_day.strftime("%a")
    return f"Wczoraj był dzień: {day}"

assert yesterday() == f"Wczoraj był dzień: {(datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%a")}"

#119,120,121(122,123,124)
def yesterday1(func):
    def inner(day = None):
        if day is None:
            y_day = datetime.date.today() - datetime.timedelta(days=1)
            return func(y_day.strftime("%a"))
        else:
            return func(week[day-1][:3]) if day > 1 and day < 8 else func(week[8-1][:3])
    return inner

@yesterday1
def wczoraj(day):
    return f"Wczoraj był dzień: {day}"

assert wczoraj() == f"Wczoraj był dzień: {(datetime.date.today() - datetime.timedelta(days=1)).strftime("%a")}"
assert wczoraj(2) == "Wczoraj był dzień: Mon"
assert wczoraj(7) == "Wczoraj był dzień: Sat"
assert wczoraj(1) == "Wczoraj był dzień: Sun"

#125
def before_yesterday():
    by_day = datetime.date.today()-datetime.timedelta(days=2)
    return f"Przed wczoraj był taki dzień: {by_day.strftime("%A")}"

assert before_yesterday() == f"Przed wczoraj był taki dzień: {(datetime.date.today()-datetime.timedelta(days=2)).strftime("%A")}"

#126,127,128(129,130,131)
week= {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
def bf_yesterday(func):
    def inner(day = None):
        if day is None:
            bfy_day = datetime.date.today() - datetime.timedelta(days=2)
            return func(bfy_day.strftime("%A"))
        else:
            pw= (day-2)% 7
            pw= 7 if pw == 0 else pw
            return func(week[pw])
    return inner

@bf_yesterday
def przedwczoraj(day):
    return f"Przed wczoraj był taki dzień: {day}"

assert przedwczoraj() == f"Przed wczoraj był taki dzień: {(datetime.date.today() - datetime.timedelta(days=2)).strftime("%A")}"
assert przedwczoraj(1) == "Przed wczoraj był taki dzień: Saturday"
assert przedwczoraj(2) == "Przed wczoraj był taki dzień: Sunday"
assert przedwczoraj(3) == "Przed wczoraj był taki dzień: Monday"

#132
def after_tomorrow():
    at_day = datetime.date.today()+ datetime.timedelta(days=2)
    return f"Po jutrze bedzie taki dzień: {at_day.strftime("%A")}"
assert after_tomorrow() == f"Po jutrze bedzie taki dzień: {(datetime.date.today()+ datetime.timedelta(days=2)).strftime("%A")}"

#133,134,135(136,137,138)
def after_tomorrow2(func):
    def inner(day = None):
        if day is None:
            at_day = datetime.date.today() + datetime.timedelta(days=2)
            return  func(at_day.strftime("%A"))
        else:
            at_day = (day + 2) % 7
            return func(week[at_day])
    return inner

@after_tomorrow2
def pojutrze(day):
    return f"Po jutrze bedzie taki dzień: {day}"

assert pojutrze() == f"Po jutrze bedzie taki dzień: {(datetime.date.today() + datetime.timedelta(days=2)).strftime("%A")}"
assert pojutrze(1) == "Po jutrze bedzie taki dzień: Wednesday"
assert pojutrze(6) == "Po jutrze bedzie taki dzień: Monday"
assert pojutrze(7) == "Po jutrze bedzie taki dzień: Tuesday"
