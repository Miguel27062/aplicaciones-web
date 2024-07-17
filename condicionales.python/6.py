import math

def calcular_area(figura):
    if figura == 1:  
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
    elif figura == 2: 
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado * lado
    elif figura == 3:  
        base = float(input("Ingrese la base del paralelogramo: "))
        altura = float(input("Ingrese la altura del paralelogramo: "))
        area = base * altura
    elif figura == 4:  
        diagonal1 = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal2 = float(input("Ingrese la diagonal menor del rombo: "))
        area = (diagonal1 * diagonal2) / 2
    elif figura == 5:  
        base_mayor = float(input("Ingrese la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        area = ((base_mayor + base_menor) / 2) * altura
    elif figura == 6: 
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
    elif figura == 7:  
        lado = float(input("Ingrese el lado del triángulo equilátero: "))
        area = (lado**2 * math.sqrt(3)) / 4
    elif figura == 8:  
        cateto1 = float(input("Ingrese el cateto 1 del triángulo rectángulo: "))
        cateto2 = float(input("Ingrese el cateto 2 del triángulo rectángulo: "))
        area = (cateto1 * cateto2) / 2
    elif figura == 9:  
        perimetro = float(input("Ingrese el perímetro del polígono regular: "))
        apotema = float(input("Ingrese el apotema del polígono regular: "))
        area = (perimetro * apotema) / 2
    else:
        print("Opción inválida.")
        return

    print("El área de la figura es:", area)


print("Calculadora de áreas de figuras geométricas")
print("1. Rectángulo")
print("2. Cuadrado")
print("3. Paralelogramo")
print("4. Rombo")
print("5. Trapecio")
print("6. Triángulo")
print("7. Triángulo equilátero")
print("8. Triángulo rectángulo")
print("9. Polígono regular")

opcion = int(input("Seleccione la figura (1-9): "))
calcular_area(opcion)
