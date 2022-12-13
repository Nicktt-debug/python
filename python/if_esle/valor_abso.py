""" 
Fes un programa que llegeixi un nombre i digui quin dia de la setmana és. Per
exemple, el 0 és dilluns, el 1 és dimarts, etc...
Fixa’t que, com sempre, segons el joc de proves el programa canvia. """

num = int(input("dime dia: "))
dia = str("hoy es dia ")

if num == 0:
    print(dia + "lunes")
elif num == 1:
    print(dia + "martes")
elif num == 2:
    print(dia + "miercoles")
elif num == 3:
    print(dia + "jueves")
elif num == 4:
    print(dia + "viernes")
elif num == 5:
    print(dia + "sabado")
elif num == 6:
    print(dia + "domingo")
else:
    print("error")