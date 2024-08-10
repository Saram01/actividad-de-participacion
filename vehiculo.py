class vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

mi_vehiculo = vehiculo(90, 15000)
print("Velocidad maxima:", mi_vehiculo.velocidad_maxima)
print("Kilometraje:", mi_vehiculo.kilometraje)