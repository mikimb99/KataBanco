import unittest
from cuenta import Cuenta
from cuenta import Excepcion
class Tests(unittest.TestCase):

    def test_cuentanueva(self):
        cuenta = Cuenta()
        self.assertEqual(cuenta.saldo,0)
    def test_ingreso_cuentanueva(self): #esta cuenta no tiene saldo
        cuenta = Cuenta()
        cuenta.ingresar(200)
        self.assertEqual(cuenta.saldo,200)
    def test_ingreso_cuentaconsaldo(self): #esta cuenta si tiene saldo
        cuenta = Cuenta()
        cuenta.saldo=1000
        cuenta.ingresar(200)
        self.assertEqual(cuenta.saldo,1200)
    def test_retirodinero_teniendo(self): #solo puedo retirar si ya tengo pasta
        cuenta = Cuenta()
        cuenta.saldo = 500
        cuenta.retirar(200)
        self.assertEqual(cuenta.saldo,300)

    def test_error_nodinero_suficiente(self): #excepción si no tengo dinero
        cuenta = Cuenta()
        cuenta.saldo = 400
        cuenta.retirar(800)
        try:
            cuenta.dinero_neg(cuenta.saldo)
        except Excepcion:
                pass
        else:
                self.fail("mierda")

    #def test_cantidad_limitesup(self): #comprobacion de test cantidad >500 salta excepcion, CORRECTO
     #   cuenta = Cuenta()
        #  cuenta.saldo= 700
        #cuenta.cantidad_diaria_limit(600)
        #try:
        #   cuenta.cantidad_diaria_limit(cuenta.saldo)
        #except Excepcion:
        #   pass
        #else:
    #       self.fail("No va")

    def test_cantidad_limitebien(self): #comprobacion de test cantidad correcta
        cuenta = Cuenta()
        cuenta.saldo= 700
        cuenta.cantidad_diaria_limit(400)
        try:
            cuenta.cantidad_diaria_limit(cuenta.saldo)

        except Excepcion:
            pass
        else:
            self.fail("No va")


    if __name__ == '__main__':
           unittest.main()


