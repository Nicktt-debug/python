pass1 = input("Enter password: ")
pass2 = input("Enter password again: ")

if pass1 == pass2:
    if len(pass1) > 8:
        if pass1[0] >= "A" and pass1[0] <= "Z":
            print("Contrasenya vàlida")
        else:
            print("La contrasenya no comença amb una contrasenya majúscula")
    else:
        print("La contrasenya és massa curta")
else:
    print("contraseña no valida")
