vuodenajat = (
    "talvi", "talvi", "kevät",
    "kevät", "kevät", "kesä",
    "kesä", "kesä", "syksy", 
    "syksy", "syksy", "talvi"
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    # Vähennetään 1, koska monikon indeksointi alkaa nollasta
    print(vuodenajat[kuukausi - 1])

else:
    print("Virheellinen kuukauden numero! Anna luku väliltä 1-12.")