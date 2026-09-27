tuuma = 2.54
while tuuma >= 0:
    sentit = tuuma * 2.54
    print(sentit, "tuumaa")
    tuuma = float(input("Anna sentit: "))
    if tuuma < 0:
        print("Ohjelma lopettettu.")