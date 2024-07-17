def convertir_temperatura():
    print("Conversor de Temperaturas")
    print("1. Fahrenheit a Celsius")
    print("2. Fahrenheit a Kelvin")

    print("16. Réaumur a Rankine")

    opcion = int(input("Seleccione la opción de conversión: "))

    valor = float(input("Ingrese el valor a convertir: "))

    if opcion == 1:
    
        resultado = (valor - 32) / 1.8
        print(f"{valor} °F equivalen a {resultado} °C")
    elif opcion == 2:
    
        resultado = (valor + 459.67) / 1.8
        print(f"{valor} °F equivalen a {resultado} K")
    
    else:
        print("Opción inválida.")

convertir_temperatura()
