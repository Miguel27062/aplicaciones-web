nombre = input("por favor ingrese su nombre: ")
edad = input("por favor ingrese su edad:")

if not edad.isdigit():
    print("por favor ingrese su edad en numero enteros.")

else:
    edad = int(edad)
    if edad < 18:
        print("usted es menor de edad")

    else:
        print("usted es mayor de edad.")
        