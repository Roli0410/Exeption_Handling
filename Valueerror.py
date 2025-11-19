
try: 
    szam = int(input("Kérlek adj meg egy egész számot! "))
    print(f"A szám négyzete: {szam ** 2}")
except ValueError:
    print("Nem számot adtál meg")

print("OK")