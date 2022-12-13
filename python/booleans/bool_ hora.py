h = int(input("hora: "))
m = int(input("min: "))
s = int(input("sec: "))

if h >= 0 and h <= 23 and m >= 0 and m <=59 and s >= 0 and  s <= 59:
    print(True)
else:
    print(False)