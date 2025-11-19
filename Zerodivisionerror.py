
try:
    osztando = 10
    oszto = int(input(f"Mennyivel osszam el a(z) {osztando} számot? "))
    print(f"A két szám osztásának eredménye: {osztando/oszto}")
except ZeroDivisionError:
    print("Nullával nem oszthatunk")