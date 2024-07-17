
notas = []
for i in range(5):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i+1} (de 0.0 a 5.0): "))
            if 0.0 <= nota <= 5.0:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

promedio = sum(notas) / len(notas)

if promedio >= 3.0:
    print(f"Promedio: {promedio:.2f} - Aprobó")
else:
    print(f"Promedio: {promedio:.2f} - No aprobó")
