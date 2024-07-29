class Potencia:

    def __init__(self, base, exponente):

        if not isinstance(exponente, int) or exponente < 0:
            raise ValueError("Ingresar un exponente entero no negativo.")
        self.base = base
        self.exponente = exponente

    def calcular_potencia(self):

        resultado = 1
        for _ in range(self.exponente):
            resultado *= self.base
        return resultado

potencia = Potencia(2, 3)
resultado = potencia.calcular_potencia()
print(f"2 elevado a la potencia de 3 es: {resultado}")
