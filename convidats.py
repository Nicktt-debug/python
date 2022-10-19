
convidats = int(input("convidats: "))

taulasde12 = convidats // 12
a = 12 * taulasde12
taulasobre = convidats - a
13
print("tablas de 12: ", taulasde12)

if taulasobre != 0:
    print("tablas totales: ", taulasde12 +1)
else:
    print("tablas de 12: ", taulasde12)

print ("numero de personas en tabla extra : " , taulasobre)
#print("tablas de 12: ", taulasde12)
