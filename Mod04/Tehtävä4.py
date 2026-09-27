import random
numero= int(random.randint(0, 10))
while True:
    arvaus = int(input("Arvaa numero väliltä 0-10: "))
    if arvaus == numero:
        print("Oikein!")
        break
    else:
        print("Väärä luku.")

