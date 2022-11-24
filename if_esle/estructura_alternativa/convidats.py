""" Recordeu el problema que tenia en una activitat anterior:
Em vull casar la setmana vinent i tinc un problema amb les taules i els convidats. He
pensat en convidar 431 persones i m'agradaria fer taules de 12 persones. Com que
els informàtics som molt metòdics i frikis, vull que a cada taula hi hagi exactament
12 convidats excepte possiblement en una taula, on hi posaré els convidats que
'sobrin'.
Vull fer un programa que em llegeixi el nombre de convidats, em digui les taules que
necessitaré i de quantes persones serà la 'taula diferent'.
Un alumne havia fet el següent joc de proves, i va tenir problemes perquè no
aconseguia verificar-lo només amb estructura seqüencial. S’ha posat molt content
perquè ara si que pot fer un programa que s’adeqüi a aquest joc de proves.
EE: nombres enters >= 2 (els nuvis com a mínim)
Entrada Sortida
convidats Taules Persones a la taula diferent
38 4 2
431 36 11
6 1 6
24 2 0
Fes un programa que concordi amb aquest joc de  """


convidats = int(input("convidats: "))

taulasde12 = convidats // 12

taulasobre = convidats % 12

print("tablas de 12: ", taulasde12)

if taulasobre != 0:
    print("tablas totales: ", taulasde12 +1)
else:
    print("tablas de 12: ", taulasde12)

print ("numero de personas en tabla extra : " , taulasobre)
