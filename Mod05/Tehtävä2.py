luvut = []

luku = input("Anna kokonaisluku(tyhjä lopettaa):")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna kokonaisluku(tyhjä lopettaa):")

luvut.sort(reverse=True)
viisi_suurinta = luvut[:5]
print("Viisi suurinta:", viisi_suurinta)