#Kirjoita ohjelma, joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän. Ohjelma tulostaa
#päiväpalkan, joka on tuntipalkka kerrottuna tehdyillä tunneilla, paitsi sunnuntaina, jolloin
#tuntipalkka on kaksinkertainen.


t_tunnit = input("Anna tehdyt tunnit:")
t_tunnit_float = float(t_tunnit)
vkp = input("Anna viikonpäivä: ")
tuntipalkka = input("Anna tuntipalkka: ")
tuntipalkka_float = float(tuntipalkka)
if vkp == "su":
    pv_palkka = tuntipalkka_float * t_tunnit_float * 2
else:
    pv_palkka = tuntipalkka_float * t_tunnit_float
print(f"Päiväpalkka: {pv_palkka}")