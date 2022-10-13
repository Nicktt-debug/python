# falta de asistencia
faltas = int(input("1 si es mayor que 25% y 0 si menor: "))

#pide las 3 notas

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

#calculo de nota

notaFinal = (nota1 + nota2 + nota3) / 3

# print nota final
if faltas == 0:
    print(notaFinal)
else:
    notaFinal = 0
    print(notaFinal)
