class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        print("Realiza un deposito en la cuenta.")
        if monto > 0:
            self.balance += monto
            print(f"Se ha depositado ${monto}. Nuevo balance: ${self.balance}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        print("Realiza un retiro de la cuenta.")
        if monto > 0:
            if monto <= self.balance:
                self.balance -= monto
                print(f"Se ha retirado ${monto}. Nuevo balance: ${self.balance}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("El monto a retirar debe ser mayor que cero.")

    def cuota_manejo(self):
        print("Aplica un porcentaje del 2% sobre el balance de la cuenta como cuota de manejo.")
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se ha aplicado una cuota de manejo de ${cuota}. Nuevo balance: ${self.balance}")

    def detalles(self):
        print("Imprime los detalles de la cuenta bancaria.")
        print(f"Detalles de la cuenta:\n"
              f"Numero de cuenta: {self.numero_cuenta}\n"
              f"Propietarios: {', '.join(self.propietarios)}\n"
              f"Balance: ${self.balance}")

    def __str__(self):
        return f"Cuenta: {self.numero_cuenta}, Propietarios: {', '.join(self.propietarios)}, Balance: ${self.balance}"



cuenta1 = CuentaBancaria("123456789", ["Juan Gonzales"], 1059000.50)
cuenta2 = CuentaBancaria("987654321", ["Karla Perez"], 607008.75)


print(cuenta1)
print(cuenta2)


cuenta1.depositar(55000)
cuenta2.depositar(700500)
cuenta1.depositar(400800)
cuenta2.depositar(300778)


cuenta1.retirar(150000)
cuenta2.retirar(1000000)
cuenta1.retirar(60000)


cuenta1.cuota_manejo()
cuenta2.cuota_manejo()


cuenta1.detalles()
cuenta2.detalles()