def calcular_suma_promedio(numeros):

    suma = sum(numeros)
    promedio = suma / len(numeros)
    return suma, promedio

numeros = []
for i in range(10):
    numero = float(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(numero)

resultado = calcular_suma_promedio(numeros)

print("La suma de los números es:", resultado[0])
print("El promedio de los números es:", resultado[1])
