
ostoslista = ["leipä", "kananmuna", "maito"]

while ostoslista:
    tuote = input("Minkä tuotteen ostit?")

    if tuote in ostoslista:
        ostoslista.remove(tuote)
        print("Jäljellä olevat tuotteet,lista")
    else: print("Tuotetta ei ole listalla")
