
lux = "Lux on parvekkeellinen hytti yläkannella."
a = "A on ikkunnallinen hytti autokanne yläpuolella."
b = "B on ikkunaton hytti autokannen yläpuolella."
c = "C on ikkunaton hytti autokannen alapuolella."
luokka = input("Anna hyttiluokka (LUX, A, B tai C): ")

if luokka == "LUX":
    print(lux)
elif luokka == "A":
    print(a)
elif luokka == "B":
    print(b)
elif luokka == "C":
    print(c)
else:
    print("Virheellinen hyttiluokka")