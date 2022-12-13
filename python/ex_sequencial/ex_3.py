#!/usr/bin/python3 
#-*- coding: utf-8-*- 
# 
# Escola del Treball de Barcelona 
# Administració de Sistemes informàtics
# Curs 2022-23
# 
# Autor: muhammad ahsan
# Data: 13/12/2022
#
# Versió: 1
#
# Descripció: demanar als usuaris que introdueixin els valors dels radis dels dos 
# cercles i calcular el radi(mitjana de radis de dues circle) del tercer cercle   
#               
#               Especificacions d'entrada: 

# radi de 2 circles (float) 
#
# Joc de proves:
#						Entrada 		Sortida
#		Execució 1         12
#                          12              12.0
#		Execució 2		   5.45
#                          3.8    		4.698004895697747


# Demanar als usuaris que introdueixin els valors dels radis dels dos cercles
r1 = float(input("Introdueix el valor del primer radi: "))
r2 = float(input("Introdueix el valor del segon radi: "))

# Calcular l'àrea dels dos cercles
area1 = 3.14 * r1 ** 2
area2 = 3.14 * r2 ** 2

# Calcular l'àrea mitjana dels dos cercles
area_mitjana = (area1 + area2) / 2

# Calcular el radi del tercer cercle
r3 = (area_mitjana / 3.14) ** 0.5

# Mostrar per pantalla el valor del radi del tercer cercle
print("El valor del tercer radi és:", r3)

