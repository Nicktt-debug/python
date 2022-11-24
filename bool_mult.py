a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

pr1 = a % b == 0

segn = b // a == 0 or c // a == 0

terc = a == b and b == c

qurt = a !=  b and b!= c



print( pr1, segn, terc, qurt)