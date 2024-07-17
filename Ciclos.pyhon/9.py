def factorial(n):

  if n < 0:
    return "El factorial no está definido para números negativos."
  elif n == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, n+1):
      factorial *= i
    return factorial
numero = int(input("Ingrese un número: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
