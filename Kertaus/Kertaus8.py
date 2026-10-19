#Kirjoita ohjelma, jossa on lista viiden tuotteen valmistuskustannuksista. Ohjelma käy
#kustannukset läpi for-silmukan avulla ja tulostaa jokaisen kustannuksen. Samalla ohjelma
#laskee kaikkien tuotteiden valmistuskustannukset yhteen. Lopuksi ohjelma tulostaa
#kokonaiskustannuksen.

kustannukset = [120.50, 45.00, 310.20, 85.90, 215.00]


kokonaiskustannus = 0.0

print("Tuotteiden valmistuskustannukset:")


for kustannus in kustannukset:
    print("Kustannus: ",kustannus)
    kokonaiskustannus += kustannus

print("-" * 30)
print("Kokonaiskustannus yhteensä: ",kokonaiskustannus)