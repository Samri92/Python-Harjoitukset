#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
#sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
#per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
#ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
#yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

#ladataan kirjastot
import math

#Määritellään funktio
def laske_yksikkohinta(halkaisija, hinta):
    sade =(halkaisija/2)

    pinta_ala = math.pi *(sade**2)

    yksikkohinta = hinta / pinta_ala
    return round(yksikkohinta, 2)

#Pääohjelma
pitsan1_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija: "))
pitsan1_hinta = float(input("Anna ensimmäisen pizzan hinta: "))

pitsan2_halkaisija = float(input("Anna toisen pizzan halkaisija: "))
pitsan2_hinta = float(input("Anna toisen pizzan hinta: "))

yksikkohinta1 =laske_yksikkohinta(pitsan1_halkaisija, pitsan1_hinta)
yksikkohinta2 =laske_yksikkohinta(pitsan2_halkaisija, pitsan2_hinta)

print("Ensimmäisen pizzan yksikköhinta:", yksikkohinta1, "€")
print("Toisen pizzan yksikköhinta:", yksikkohinta2, "€")

#verrataan hintoja
if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäisellä pizzalla on parempi yksikköhinta")
elif yksikkohinta2 < yksikkohinta1:
    print("Toisella pizzalla on parempi yksikköhinta")
else:
    print("Pizzoilla on sama yksikköhinta")