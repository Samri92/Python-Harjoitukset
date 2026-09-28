print("\n----------------TERVETULOA LASKIMEEN----------------")

while True:
    print("Valitse mitä toimintoa haluat käyttää:")
    print(" 1.Yhteenlasku\n 2:Vähennyslasku\n 3:Kertolasku\n 4:Jakolaku\n 5.Lopeta\n")
    valinta = input("Valintasi: ").upper()

    if valinta =="5":
        print("Lopetetaan ohjelma")
    break

a = float(input("Anna ensimmäinen luku: "))
b = float(input("Anna toinen luku: "))

if valinta == "1":
    print(f"Lukujen {a} ja {b} summa on {a + b}")
elif valinta == "2":
    print(f"Lukujen {a} ja {b} erotus on {a - b}")
elif valinta == "3":
    print(f"Lukujen {a} ja {b} tulo on {a * b}")
elif valinta == "4":
    print(f"Lukujen {a} ja {b} osamäärä on {a / b}")
else:
    print("Virheellinen valinta")

print("Ohjelma päättynyt")