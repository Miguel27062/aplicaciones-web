numero = input("digite un numero: ")

try:
    numero = int(numero)
    if numero > 0:
        print("el numero ingresado es positivo.")
    elif numero < 0:
        print("el numero ingresado es negativo.")
    else:
        print("el numero ingresado es cero.")
except ValueError:
    print("por favor digitar un numero valido.")
