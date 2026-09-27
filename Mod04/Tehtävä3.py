pieninluku = None
suurinluku = None

while True:
    syöte = input("Anna luku: ")

    if syöte == "":
        break

    luku = int(syöte)

    if pieninluku is None or luku < pieninluku:
        pieninluku = luku
    if suurinluku is None or luku > suurinluku:
        suurinluku = luku

if pieninluku is not None:
    print("Pienin luku on:", pieninluku)
    print("Suurin luku on:", suurinluku)
