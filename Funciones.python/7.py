def esta_en_rango(inicio, numero, fin):
  return inicio <= numero <= fin
rango_inicio = 5
rango_fin = 10
numero_a_comprobar = 7

if esta_en_rango(rango_inicio, numero_a_comprobar, rango_fin):
  print(numero_a_comprobar, "está dentro del rango")
else:
  print(numero_a_comprobar, "no está dentro del rango")
