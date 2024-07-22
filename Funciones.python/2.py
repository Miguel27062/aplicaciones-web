import math

def area_cuadrado(lado):

  return lado * lado

def area_rectangulo(base, altura):

  return base * altura

def area_triangulo(base, altura):

  return (base * altura) / 2

def area_circulo(radio):
  return math.pi * radio * radio

while True:
  print("Calculadora de áreas")
  print("1. Cuadrado")
  print("2. Rectángulo")
  print("3. Triángulo")
  print("4. Círculo")
  print("5. Salir")

  opcion = int(input("Ingrese por favor una opción: "))

  if opcion == 1:
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = area_cuadrado(lado)
    print("El área del cuadrado es:", area)
  elif opcion == 2:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = area_rectangulo(base, altura)
    print("El área del rectángulo es:", area)
  elif opcion == 3:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = area_triangulo(base, altura)
    print("El área del triángulo es:", area)
  elif opcion == 4:
    radio = float(input("Ingrese el radio del círculo: "))
    area = area_circulo(radio)
    print("El área del círculo es:", area)
  elif opcion == 5:
    break
  else:
    print("Opción inválida.")
