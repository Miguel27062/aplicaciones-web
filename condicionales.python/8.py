def ordenar_numeros(num1, num2, num3):

  numeros = [num1, num2, num3]
  numeros.sort()
  print("Orden ascendente:", numeros)
  numeros.reverse()
  print("Orden descendente:", numeros)


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))


ordenar_numeros(num1, num2, num3)
