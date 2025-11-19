osztando = 10
while True: 
    try:
        oszto = int(input(f"Mennyivel osszam el a(z) {osztando} számot? "))
        print(f"A két szám osztásának eredménye: {osztando/oszto}")
        break
    except ZeroDivisionError as e:
        print(e)
        print("ZeroDivisionError: Nullával nem oszthatunk")
    except ValueError as e:
        print(e)
        print("ValueError: Nem számot adtál meg")