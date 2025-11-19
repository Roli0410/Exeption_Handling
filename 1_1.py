"""1. Feladat
Írj egy programot, ami a felhasználótól három egész számot számot kér be egyesével, ezeket eltárolja egy listában, majd a képernyőre kiírja a lista tartalmát! 
Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet, és ismétlődjön meg a bekérés!"""
# while True:
#     try:
#         v1 = int(input("Add meg az első számot: "))
#     except ValueError:
#         print("Számot adj meg")
    
#     try:
#         v2 = int(input("Add meg a második számot: "))
#     except ValueError:
#         print("Számot adj meg")
    
#     try:
#         v3 = int(input("Add meg a harmadik számot: "))
#     except ValueError:
#         print("Számot adj meg")

#     lista = [v1, v2, v3]
#     print(lista)

x = 3
szamok = []
while len(szamok) < x:
    try:
        szam = int(input(f"Adj meg {x} egész számot "))
        szamok.append(szam)
    except ValueError:
        print("Valueerror, kérlek egész számot adj meg ")

print(szamok)