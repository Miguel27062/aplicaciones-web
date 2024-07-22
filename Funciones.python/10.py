def es_primo(numero):
  if numero <= 1:
    return False
  if numero % 2 == 0 and numero > 2:
    return False
  for i in range(3, int(numero**0.5) + 1, 2):
    if numero % i == 0:
      return False
  return True
