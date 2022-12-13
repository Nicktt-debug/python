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
# Descripció: truncament superior de numero  
# Especificacions d'entrada: 

# 1 nombres real(float) positivo
#
# Joc de proves:
#						Entrada 		Sortida
#		Execució 1         3.14				4
#		Execució 2		   2.5			    3



n = float(input("Dime un numero : "))

m = (n % 1) + n

print(int(m))
