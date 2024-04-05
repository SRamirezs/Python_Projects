class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_datos(self):
        print(self.nombre)
        print(self.apellido)
        print(self.numero_cuenta)
        print(self.balance)

    def depositar(self, cantidad):
        self.balance = self.balance + cantidad
        print(f'Deposito exitoso, nuevo balance = {self.balance}')

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print(f'Retiro exitoso, su nuevo balance es {self.balance}')
        else:
            print('Valor del retiro supera su saldo bancario')


def crear_cliente():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido ')
    cuenta = input('Ingrese su numero de cuenta: ')
    balance = float(input('Ingrese su deposito inicial: '))
    return Cliente(nombre, apellido, cuenta, balance)


def inicio(cliente):
    while True:
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == '3':
            cliente.imprimir_datos()
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


cliente = crear_cliente()
inicio(cliente)
