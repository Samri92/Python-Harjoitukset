#Kirjoita ohjelma, joka simuloi tehtaan tuotantoa. Ohjelma kysyy käyttäjältä, mitä tuotetta
#valmistetaan ja kuinka monta kappaletta sitä valmistetaan. Tallenna tuotteiden nimet ja
#määrät omiin listoihinsa.Tämän jälkeen ohjelma kysyy "Jatketaanko tuotantoa?". Jos
#käyttäjä vastaa "Kyllä", ohjelma kysyy seuraavan tuotteen ja sen määrän. Ohjelma jatkaa
#kysymistä, kunnes käyttäjä syöttää "Ei".
#Kun tuotanto lopetetaan, ohjelma tulostaa kaikki valmistetut tuotteet ja niiden määrät.

tuotteet = []
maarat = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta kappaletta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatko = input("Jatketaanko tuotantoa?: ")
    if jatko == "ei":
        break
for i in range(len(tuotteet)):
    print(f"{tuotteet[i]}: {maarat[i]} kpl")

