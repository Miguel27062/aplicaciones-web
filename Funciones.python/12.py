def palindromo(cadena):
  cadena = cadena.replace(" ", "").lower()
  cadena_invertida = cadena[::-1]
  return cadena == cadena_invertida
frase = "Anita lava la tina"
if palindromo(frase):
  print(frase, "es un palíndromo.")
else:
  print(frase, "no es un palíndromo.")
