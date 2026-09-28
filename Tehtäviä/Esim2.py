nimet = ["Matti", "Teppo", "Kalle", "Jussi", "Sam"]

nimet.insert(3, "Jorma") #lisää kohtaan 3 uuden nimen
nimet2 = ["Matti", "Teppo"]

nimet.extend(nimet2) #yhdistää kaksi listaa

print(nimet)

nimet.sort() #sorttaa listan aakkosjärjestykseen

print(nimet)