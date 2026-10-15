renta = int(input("Introduzca su renta anual: "))

renta = int(input("Introduzca su renta anual: "))

if renta < 10000:
    print("pagas un 5%")
else:
    if renta < 20000:
        print("pagas un 15%")
    else:
        if renta < 35000:
            print("pagas un 20%")
        else:
            if renta < 60000:
                print("pagas un 30%")
            else:
                print("pagas un 45%")
                