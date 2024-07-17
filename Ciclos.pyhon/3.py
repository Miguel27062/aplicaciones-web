def fibonacci(n):

  fib_list = [0, 1]
  suma = 1
  if n > 1:
    for i in range(2, n):
      next_fib = fib_list[-1] + fib_list[-2]
      fib_list.append(next_fib)
      suma += next_fib
  return fib_list, suma

n = int(input("Ingrese la cantidad de términos de Fibonacci que desea calcular: "))

resultado = fibonacci(n)

print("Los primeros", n, "términos de la serie de Fibonacci son:", resultado[0])
print("La suma de estos términos es:", resultado[1])
