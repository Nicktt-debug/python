
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
# Descripció: convertir numero binari a decimal  
# Especificacions d'entrada: 

# 1 numero int de 8 digitos  positivo
#
# Joc de proves:
#						Entrada 		Sortida
#		Execució 1         10100101		165
#		Execució 2		   10001101       141


# Demanar al usuari que introdueixi un nombre binari
nombre_binari = input("Introdueix un nombre binari: ")


# Convertir el nombre binari a un valor enter
nombre_decimal = int(nombre_binari, 2)

# Mostrar per pantalla el valor decimal del nombre binari
print("El valor decimal del nombre binari és:", nombre_decimal)
