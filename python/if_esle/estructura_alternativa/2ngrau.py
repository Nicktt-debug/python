a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

result1 = 0
result2 = 0


d = b**2-4*a*c 

if a == 0:
    if b == 0:
        if c == 0:
            print("hi ha infinits solucions")
        elif c != 0:
            print("no hi ha  solucions")
        
        elif b != 0:
            x = -c/b 
            print("la solucio es:", x)
else:
    descriminant =  b**(2) - 4*a*c

    if descriminant < 0:
        print("no hi ha cap solucion")
    elif descriminant == 0:
        x1= (-b+(descriminant)**0.5)/(2*a)
        x2= (-b-(descriminant)**0.5)/(2*a)
        print("la solucio es:",x1,x2)
