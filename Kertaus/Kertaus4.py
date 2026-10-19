#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja. Jos luku on pienempi kuin nolla,
#ohjelma tulostaa viestin "Virheellinen numero". Jos luku on suurempi kuin nolla, ohjelma
#tulostaa luvun neliöjuuren Pythonin sqrt-funktiolla. Molemmissa tapauksissa ohjelma kysyy
#sen jälkeen uutta lukua. Jos käyttäjä syöttää luvun nolla, ohjelma lopettaa kysymisen ja
#poistuu silmukasta

from math import sqrt

loop1 = True
while loop1:
        kysy_numero = int(input("Anna kokonaisluku: "))
        if kysy_numero < 0:
            print("Virheellinen numero")
        if kysy_numero > 0:
              print("Neliöjuuri numerosta on: ", sqrt(kysy_numero))

        if kysy_numero == 0:
              loop1 = False
              print("Lopetetaan")
              break
