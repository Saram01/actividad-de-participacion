class Carta:
   
    PINTA_CORAZONES = "Corazones"
    PINTA_DIAMANTES = "Diamantes"
    PINTA_TREBOLES = "Treboles"
    PINTA_PICAS = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor 
        self.pinta = pinta 
        
    def __str__(self):
        return f"{self.valor} de {self.pinta}"


carta1 = Carta(9, Carta.PINTA_CORAZONES)
carta2 = Carta("K", Carta.PINTA_PICAS)

print(carta1)
print(carta2)