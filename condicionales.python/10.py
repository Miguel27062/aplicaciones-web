def calcular_costo_llantas(cantidad_llantas):

  if cantidad_llantas < 6:
    precio_unitario = 240000
  elif 6 <= cantidad_llantas <= 7:
    precio_unitario = 221000
  else:
    precio_unitario = 180000

  costo_total = cantidad_llantas * precio_unitario
  return costo_total

cantidad = int(input("Ingrese la cantidad de llantas a comprar: "))

costo = calcular_costo_llantas(cantidad)
print("El costo total de la compra es: $", costo)
