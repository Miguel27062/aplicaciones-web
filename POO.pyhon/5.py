class Ave:
    def __init__(self, color_plumaje, descripcion_general):
        self.color_plumaje = color_plumaje
        self.descripcion_general= descripcion_general

    def volar(self):
        print("ave volando")

    def comer(self):
        print("comiendo semillas.")

class Aguila(Ave):
    def cazar(self):
        print(" cazando presas.")

class Canario(Ave):
    def cantar(self):
        print("cuidando sus crias")

class Pingüino(Ave):
    def nadar(self):
        print(" nadando en el agua.")
    def volar(self):
        print("no puede volar")
aguila = Aguila("marrón", 2.5)
aguila.volar()
aguila.cazar()

canario = Canario("amarillo", 0.2)
canario.cantar()

pingüino = Pingüino("negro y blanco", 1.5)
pingüino.nadar()
pingüino.volar()
