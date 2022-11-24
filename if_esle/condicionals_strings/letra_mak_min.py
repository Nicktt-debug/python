letra = input("dime la letra: ")

if letra >= "a" and letra <= "z":
    print("es una letra minúscula")
elif letra >= "A" and letra <= "Z":
    print("es una letra mayúscula")
else:
    print("no es una letra")