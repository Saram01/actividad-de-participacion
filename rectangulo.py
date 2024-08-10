class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1  
        self.esquina2 = esquina2  

    def calcular_perimetro(self):
        largo = abs(self.esquina2.x - self.esquina1.x)
        ancho = abs(self.esquina2.y - self.esquina1.y)
        return 2 * (largo + ancho)

    def calcular_area(self):
        largo = abs(self.esquina2.x - self.esquina1.x)
        ancho = abs(self.esquina2.y - self.esquina1.y)
        return largo * ancho

    def es_cuadrado(self):
        largo = abs(self.esquina2.x - self.esquina1.x)
        ancho = abs(self.esquina2.y - self.esquina1.y)
        return largo == ancho


esquina1 = Punto(1, 1)
esquina2 = Punto(4, 5)


rectangulo = Rectangulo(esquina1, esquina2)


print("Perimetro del rectangulo:", rectangulo.calcular_perimetro())
print("Area del rectángulo:", rectangulo.calcular_area())
print("¿Es un cuadrado?", rectangulo.es_cuadrado())