#listat

nimet = ["Matti", "Teppo", "Kalle", "Jussi", "Sam"]

nimet.insert(3, "Jorma") #lisää kohtaan 3 uuden nimen
nimet2 = ["Matti", "Teppo"]

nimet.extend(nimet2) #yhdistää kaksi listaa
print(nimet)
# nimet.remove("Kalle") #poistaa listasta Kallen
print(nimet.index("Matti"))

if "Matti" in nimet:
    print("Matti löytyy listasta")

print(nimet)