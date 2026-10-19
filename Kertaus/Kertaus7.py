#Kirjoita ohjelma, joka laskee, kuinka monessa sanassa listassa on enemmän kuin 5
#kirjainta.
#Luo lista itse ja käytä len()-funktiota sanojen pituuden tarkistamiseen

sanat = ["kissa", "aurinkoinen", "talo", "ohjelmointi", "puu", "tietokone", "koira"]

laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print(f"Sanat: {sanat}")
print(f"Sanoja, joissa on enemmän kuin 5 kirjainta: {laskuri}")