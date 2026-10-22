
tipo = input("desea una pizza vegetariana? (escriba si o no): ").lower()

if tipo == "si" or tipo == "s":

    opcion = input("elija un numero de ingrediente (pimiento(1) o tofu(2)): ")
    
    if opcion == "1":
        ingrediente_extra = "pimiento"
    elif opcion == "2":
        ingrediente_extra = "tofu"

    print("tipo de pizza: vegetariana")
    print(f"ingredientes: mozzarella, tomate y {ingrediente_extra}.")

else:
    
    opcion = input("elija un numero de ingrediente (peperoni(1), jamon(2) o salmon(3)): ")
    
    if opcion == "1":
        ingrediente_extra = "peperoni"
    elif opcion == "2":
        ingrediente_extra = "jamon"
    elif opcion == "3":
        ingrediente_extra = "salmon"

    print("tipo de pizza: no vegetariana")
    print(f"ingredientes: mozzarella, tomate y {ingrediente_extra}.")