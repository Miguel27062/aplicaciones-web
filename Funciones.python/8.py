def contarlasmayusculas_minusculas(cadena):

  mayusculas = 0
  minusculas = 0

  for caracter in cadena:
    if caracter.isupper():
      mayusculas += 1
    elif caracter.islower():
      minusculas += 1

  return mayusculas, minusculas
cadena = "Hola, Mundo! ¿Cómo estás?"
resultado = contarlasmayusculas_minusculas(cadena)
print("Mayúsculas:", resultado[0])
print("Minúsculas:", resultado[1])
