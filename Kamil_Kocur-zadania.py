
# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH

# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

def postcode_generator(list_start='79-900', list_end='80-155'):
    parse = lambda x: int(x.replace('-', ""))
    list_start, list_end = parse(list_start), parse(list_end)
    return['{0[0]:02d}-{0[1]:03d}'.format((divmod(postcode, 1000))) for postcode in range(list_start+1, list_end)]

print(postcode_generator('79-900', '80-155'))

# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE

# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

def check_missing_values(list_to_check, list_range):
    return list(set(range(1, list_range+1)) - set(list_to_check))

print(check_missing_values([2,3,7,4,9], 10))

# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

from decimal import Decimal
def generate_step_list():
    return [Decimal(x/2) for x in range(4, 12, 1)]


print(generate_step_list())
