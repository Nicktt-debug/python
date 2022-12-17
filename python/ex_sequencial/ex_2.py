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
# Descripció: print 1 si radi de dos cercles son iguals y 0 si no son iguals  
#               
#               Especificacions d'entrada: 

# radi de 2 circles (float) 
#
# Joc de proves:
#						Entrada 		Sortida
#		Execució 1         35
#                           34              0
#		Execució 2		   2.5
#                           2.5    			 1





r1 = float(input("radi de 1r circle : "))
r2 = float(input("radi de 2n circle : "))

pi = 3.14


a1 = pi * r1**2
a2 = pi * r2**2

print(int(a1 == a2))