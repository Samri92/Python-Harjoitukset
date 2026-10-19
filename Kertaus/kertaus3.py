#Kirjoita ohjelma, joka simuloi tuotantolinjan toimintaa. Ohjelma tulostaa viestin "Tuote
#valmistettu!" ja kysyy sen jälkeen "Jatketaanko tuotantoa?" niin kauan, kunnes käyttäjä
#syöttää "Ei". Tämän jälkeen ohjelma tulostaa "Tuotanto lopetettu!" ja päättyy

while True:
    print("Tuote valmistettu!")
    input1 = input("Jatketaanko tuotantoa? ")
    if input1 == "Ei":
        print("Tuotanto lopetettu!")
        break