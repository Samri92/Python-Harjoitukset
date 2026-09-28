
luku = int(input("Anna luku:"))
alkuluku = luku > 1

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        alkuluku = False
        break

if alkuluku:
    print(f"luku {luku} on alkuluku ")
else:
    print(f"Luku {luku} ei ole alkuluku.")

