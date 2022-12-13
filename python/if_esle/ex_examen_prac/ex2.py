
# capçalera complerta

'''
joc de proves
Entrada 			sortida
10, 5				True
5, 10				True
3,  2				False
-10, -2				True
-3, 2				False
-10, 5				True

Especificacions d'Entrada: 2 nombres enters diferents de 0
'''

#ATENCIÓ: Aquest programa ha de seguir aquest refinament. En cas contrari,
#serà un zero ni que funcioni correctament

#llegim dos enters
n1 = int(input())
n2 = int(input())

#els modifiquem (si cal) per tenir els valors absoluts del dos nombres 
n1 = (n1**2)**(1/2)
abss = abs(n1)
print(n1)
print(abss)

#intercanviem les variables (si cal) perquè el primer sigui major que el 
#segon

#mostrem si el segon és divisor del primer o no
print(n1 % n2 == 0)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))




