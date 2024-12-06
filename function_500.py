# Cześć masz napisać jak najwięcej fukncji(500). Powodzenia :)

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