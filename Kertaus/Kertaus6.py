#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään arvoja ja lisää ne listaan. Jokaisen
#lisäyksen jälkeen lista tulostetaan kahdella tavalla: lisäysjärjestyksessä ja pienimmästä
#suurimpaan järjestettynä. Ohjelma lopettaa, kun käyttäjä syöttää 0.

lista = []

while True:
    arvo = float(input("Anna lisättävä arvo: "))
    
    if arvo == 0:
        print("Lopetetaan")
        break

    lista.append(arvo)

print("lista lisäysjärjestyksessä")
print(lista)
print(" ")
print("Lista pienimmästä suurimpaan")
print(sorted(lista))