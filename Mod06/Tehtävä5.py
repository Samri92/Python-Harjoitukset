#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa
#toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä
#on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot
#listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def poista_parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

#Pääohjelma
lista = [3, 9, 2, 3, 5, 8, 10]

karsittu_lista = poista_parittomat(lista)

print("Alkuperäinen lista ", lista )
print("Karsittu lista: ", karsittu_lista)

