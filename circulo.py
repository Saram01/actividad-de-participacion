import math

class Circulo:
    def __init__(self, a_centro, b_centro, radio):
        self.a_centro = a_centro  
        self.b_centro = b_centro  
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def pertenece(self, a, b):
        
        distancia = math.sqrt((a - self.a_centro) ** 2 + (b - self.b_centro) ** 2)
        return distancia <= self.radio


a_centro = 0
b_centro = 0
radio = 5
circulo = Circulo(a_centro, b_centro, radio)

print("Area del circulo:", circulo.calcular_area())
print("Perimetro del circulo:", circulo.calcular_perimetro())


punto1 = (3, 4)
punto2 = (6, 6)

if circulo.pertenece(*punto1):
    print(f"El punto {punto1} pertenece al circulo.")
else:
    print(f"El punto {punto1} no pertenece al circulo.")

if circulo.pertenece(*punto2):
    print(f"El punto {punto2} pertenece al circulo.")
else:
    print(f"El punto {punto2} no pertenece al circulo.")