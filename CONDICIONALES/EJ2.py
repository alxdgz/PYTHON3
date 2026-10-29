contraseña = "admin"
repetir = input("Repite la contraseña: ")
if contraseña.lower() == repetir.lower():
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")