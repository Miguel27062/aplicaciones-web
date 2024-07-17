def calcular_precio_pizza(tamano):

  if tamano == 1:
    precio = 15000
  elif tamano == 2:
    precio = 24000
  elif tamano == 3:
    precio = 36000
  else:
    print("Tamaño de pizza inválido. Por favor, ingrese 1, 2 o 3.")
    return None  
  return precio


tamano_pizza = int(input("Ingrese el tamaño de la pizza deseada(1, 2 o 3): "))


precio_total = calcular_precio_pizza(tamano_pizza)
if precio_total is not None:
  print("El precio de la pizza es: $", precio_total)
