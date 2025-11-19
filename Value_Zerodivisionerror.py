try:
    osztando = 10
    oszto = int(input(f"Mennyivel osszam el a(z) {osztando} számot? "))
    print(f"A két szám osztásának eredménye: {osztando/oszto}")
except ZeroDivisionError as e:
    print(e)
    print("ZeroDivisionError: Nullával nem oszthatunk")
except ValueError as e:
    print(e)
    print("ValueError: Nem számot adtál meg")