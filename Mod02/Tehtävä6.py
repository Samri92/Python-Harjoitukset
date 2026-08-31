#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
#Vihje: tutustu random.randint()-funktion käyttöön.
import random

koodi1 = random.randint(0, 9)
koodi2 = random.randint(0, 9)
koodi3 = random.randint(0, 9)
print("Kolmenumeroisen koodin numerot ovat:", koodi1, koodi2, koodi3)
koodi4 = random.randint(1, 6)
koodi5 = random.randint(1, 6)
koodi6 = random.randint(1, 6)
koodi7 = random.randint(1, 6)
print("Nelinumeroisen koodin numerot ovat:", koodi4, koodi5, koodi6, koodi7)