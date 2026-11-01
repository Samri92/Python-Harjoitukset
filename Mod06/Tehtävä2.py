#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
#yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 20-tahkoista
#roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan
#pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä
#ohjelman suorituksen alussa

#Tuodaan kirjastot
import random

#Määritellään funktio
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maximi = int(input("Anna nopan tahkojen määrä: "))

tulos = 0

#Pääohjelma
while tulos != maximi:
    tulos = heita_noppaa(maximi)
    print("Heiton tulos:", tulos)
