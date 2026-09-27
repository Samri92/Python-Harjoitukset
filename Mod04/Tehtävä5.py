oikeatunnus = str("käyttäjätunnus")
oikeasalasana = str("salasana")

yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == oikeatunnus and salasana == oikeasalasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")

