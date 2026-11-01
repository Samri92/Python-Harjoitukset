#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
#ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
#gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä funktiota
#hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää
#negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

import math

def gallona_litroina(gallonat):
    return gallonat * 3.785

#Pääohjelma

while True:
    maara = float(input("Anna gallonat (negatiivinen lopettaa): "))
    if maara < 0:
        print("Ohjelma lopetettu.")
        break

    litrat = gallona_litroina(maara)
    print("Litroina:", litrat)