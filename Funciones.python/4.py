def multiplicar_lista(lista_numeros):

  producto = 1
  for numero in lista_numeros:
    producto *= numero
  return producto
mi_lista = [8, 2, 3, -1, 7]
resultado = multiplicar_lista(mi_lista)
print("El producto de los números es:", resultado)
