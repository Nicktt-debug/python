""" Escriu una expressió boolena que indiqui que tres dades enteres corresponents a un
dia, un mes i un any corresponen a una data de la tardor d’aquest any.
La tardor comença el dia 21 de setembre i l’hivern el 22 de desembre. """

dia = int(input("dime un dia: "))
mes = int(input("dime un mes: "))
any = int(input("dime un any: "))

""" if mes == 10 or mes == 11 and any == 2022:
    print(True)
elif mes == 9 and dia >= 21 and any == 2022:
    print(True)
elif mes == 12 and dia <= 22 and any == 2022:
    print(True)
else:
    print(False) """

tardor = (mes == 9 and dia >= 21 and dia <= 30 ) or (mes == 10 and dia >= 1 and dia <= 31) or (mes == 11 and dia >= 1 and dia <= 30) or (mes == 12 and dia >= 1 and dia <= 21) and any == 2022
print   (tardor)