#Kirjoita ohjelma, joka pyytää käyttäjältä sanoja. Jos käyttäjä kirjoittaa sanan "loppu",
#ohjelma tulostaa muodostuneen tarinan ja lopettaa.

lista = []

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")

    if sana == "loppu":
        break

    if lista and sana == lista[-1]:
        break
    lista.append(sana)

tarina = " ".join(lista)
print(tarina)
