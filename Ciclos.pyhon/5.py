def tabla_multiplicar(numero):

  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

tabla_multiplicar(numero)
