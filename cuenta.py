import unittest


class Excepcion(Exception):
    pass


class Cuenta(unittest.TestCase):
    saldo = 0
    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        self.saldo = self.saldo - cantidad

    def dinero_neg(self, cantidad):  # excepcion cuando tienes saldo negativo
        if self.saldo < 0:
            raise Excepcion('Saldo negativo')
        else:
            self.saldo= self.saldo- cantidad

    def cantidad_diaria_limit(self, cantidad):  # limite de 500€ retiro diario

        if self.saldo > 0 and self.saldo>cantidad <= 500:
            self.saldo = self.saldo - cantidad
        elif self.saldo > 0 and self.saldo > cantidad > 500: #limite >500 si funciona, esta excepcion si va
            raise Excepcion('Límite de retiro diario')
        else:
            raise Excepcion('Saldo negativo')
