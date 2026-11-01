#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
#silmäluvun väliltä 1-6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes
#tulee kutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

#Tuodaan kirjastot
import random

#Määritellään funktio
def heita_noppaa():
    return random.randint(1, 6)

#Pääohjelma
while True:
    tulos = heita_noppaa()
    print("Heiton tulos:", tulos)

    if tulos == 6:
        break
