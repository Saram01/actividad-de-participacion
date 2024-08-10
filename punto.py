import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return distancia

punto1 = Punto(3, 4)
punto2 = Punto(7, 1)

punto1.mostrar()
punto2.mostrar()

distancia = punto1.calcular_distancia(punto2)
print(f"La distancia entre los puntos es: {distancia}")