def pulsaciones_del_ser_humano(edad, genero):
  if genero == 1:
    pulsaciones = (220 - edad) / 10
  elif genero == 2:
    pulsaciones = (210 - edad) / 10
  else:
    return "Género no válido. Por favor, ingrese 1 para femenino o 2 para masculino."

  return pulsaciones

edad = int(input("Ingrese su edad: "))
genero = int(input("Ingrese su género (1: femenino, 2: masculino): "))

pulsaciones = pulsaciones_del_ser_humano(edad, genero)
if isinstance(pulsaciones, str):
  print(pulsaciones)
else:
  print("El número de pulsaciones por cada 10 segundos de ejercicio debe ser:", pulsaciones)
