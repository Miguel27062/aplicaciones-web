def calcular_total_a_pagar(cantidad, precio_unitario_original):

  if cantidad <= 5:
    descuento = 0
  elif 5 < cantidad < 10:
    descuento = 0.05  
  else:
    descuento = 0.08  

  precio_unitario_con_descuento = precio_unitario_original * (1 - descuento)
  total_a_pagar = cantidad * precio_unitario_con_descuento
  return total_a_pagar


cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
precio_unitario = float(input("Ingrese el precio unitario original: $"))


total = calcular_total_a_pagar(cantidad_articulos, precio_unitario)
print("El valor total a pagar es: $", total)
