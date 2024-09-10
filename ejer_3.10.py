class Cuenta:
    def __init__(self, saldo):
        """Inicializa la cuenta con un saldo."""
        self.saldo = saldo

    def calcular_interes(self):
        """Calcula el interés basado en el saldo actual."""
        if self.saldo < 10000.00:
            self.saldo *= 1.03  # 3% de interés si el saldo es menor de 10,000
        else:
            self.saldo *= 1.04  # 4% de interés si el saldo es mayor o igual a 10,000

    def mostrar_saldo_final(self):
        """Muestra el saldo final con formato."""
        print("Saldo final es %5.2f" % self.saldo)

# Ejemplo de uso
print("Dame saldo actual: ")
saldo_inicial = float(input())

mi_cuenta = Cuenta(saldo_inicial)
mi_cuenta.calcular_interes()
mi_cuenta.mostrar_saldo_final()
