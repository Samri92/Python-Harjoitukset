#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa
#listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot
#listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(luvut):
    yhteensa = 0
    for luku in luvut:
        yhteensa += luku
    return yhteensa

#Pääohjelma
lista = [3, 9, 2, 3, 5]

tulos = summa(lista)

print("Lista luvuista: ", lista )
print("Summa on : ", tulos)

