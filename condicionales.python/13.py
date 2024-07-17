def imc(peso, estatura):

  imc = peso / (estatura * estatura)

  if imc < 18.5:
    return "Bajo peso, comer mas arroz con huevo"
  elif 18.5 <= imc < 25:
    return "Normal"
  elif 25 <= imc < 30:
    return "Sobrepeso"
  elif 30 <= imc < 35:
    return "Obesidad Grado 1"
  elif 35 <= imc < 40:
    return "Obesidad Grado 2"
  elif 40 <= imc < 50:
    return "Obesidad Grado 3"
  else:
    return "Obesidad Grado 4"


peso = float(input("Ingrese el peso en kilogramos: "))
estatura = float(input("Ingrese la estatura en metros: "))

estado = imc(peso, estatura)


print("Tu IMC es:", imc)
print("Tu estado es:", estado)
