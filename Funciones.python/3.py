def sumar_lista(lista_numeros):

  suma = 0
  for numero in lista_numeros:
    suma += numero
  return suma
mi_lista = [8, 2, 3, 0, 7]
resultado = sumar_lista(mi_lista)
print("La suma de los números es:", resultado)
