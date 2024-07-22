def invertir_cadena(cadena):
  cadena_invertida = ""
  for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]
  return cadena_invertida
cadena_original = "1234abcd"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
