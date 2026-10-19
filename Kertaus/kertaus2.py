#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun. Jos luku on jaollinen kolmella,
#ohjelma tulostaa ”kolmella jaollinen”. Jos luku on jaollinen viidellä, ohjelma tulostaa "viidellä
#jaollinen". Jos luku on jaollinen sekä kolmella että viidellä, ohjelma tulostaa ”jaollinen
#molemmilla luvuilla!"

kokonaisluku = int(input("Anna kokonaisluku: "))

if kokonaisluku % 3 == 0 and kokonaisluku % 3 == 0:
    print("kolmella ja viidellä jaollinen")
elif kokonaisluku % 5 == 0:
    print("viidellä jaollinen")
elif kokonaisluku % 3 == 0:
    print("3 jaollinen")
else:
    print("Ei jaollinen 3 tai 5")