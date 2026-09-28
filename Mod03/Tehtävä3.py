
sukupuoli = input("Kerro sukupuolesi (mies/nainen): ")
hemo = int(input("Anna hemoglobiiniarvosi: "))

if sukupuoli == "mies":
    if hemo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

elif sukupuoli == "nainen":
    if hemo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
