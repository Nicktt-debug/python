""" Determina si un número enter positiu n representa un any de traspàs. Un any és de
traspàs si és múltiple de 4, excloent-ne els múltiples de 100 que no ho són de 400;
per exemple 1964, 2004 i 2400 són de traspàs, però 1977 i 2100 no. """


any = int(input("ANY: "))

""" if (any % 400 == 0) and (any % 100 == 0):
    print("{0} es traspas ".format(any))


elif (any % 4 ==0) and (any % 100 != 0):
    print("{0} es traspas".format(any))
else:
    print("{0} no es traspas".format(any)) """

any = (any % 400 == 0) and (any % 100 == 0) or (any % 4 ==0) and (any % 100 != 0)
print(any)