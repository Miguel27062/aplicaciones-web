def imprimirnumerosapares(lista):

  for numero in lista:
    if numero % 2 == 0:
      print(numero)
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
imprimirnumerosapares(mi_lista)
