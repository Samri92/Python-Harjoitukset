#Yksi leiviskä on 20 naulaa. 
#Yksi naula on 32 luotia. 
#Yksi luoti on 13,3 grammaa.

le = float(input ("Anna leiviskät."))
na = float(input ("Anna naulat."))
lu = float(input ("Anna luodit."))

luoti_g = 13.3 # on grammaa
naula = 32.0 #naula on 32 luotia
leiviskä = 20.0 # on 20 naulaa

luodit = (le * leiviskä * naula) + (na * naula) + (lu)
grammat = luodit * luoti_g

kilot = int(grammat // 1000)
grammat_jäljel = grammat % 1000
print("Massa on:", kilot,"kg", "ja", grammat_jäljel,"g")
