class BankAccount: #crearemos la clase BankAccount
    # Atributo de clase
    bank = "Central Bank"

    def __init__(self, client, balance): #definiremos el metodo constructor con los atributos de client y balance.
        self.client = client #se guardara el nombre del cliente.
        self.balance = balance #se guardara el balance del cliente.

    # Método de instancia
    def show_balance(self): #aqui se mostrara el balance o saldo del cliente.
        print(f"Customer: {self.client} - balance: ${self.balance} USD") #se imrpimira el nombre del cliente y su saldo.

    # Método de clase
    @classmethod #indica que el metodo pertenece a la clase.
    def show_bank(cls): #recibe la clase para acceder a sus atributos.
        print(f"Bank: {cls.bank}") #se imprimira el nombre del banco al que pertenece la cuenta.

    # Método estático
    @staticmethod #indica que el metodo pertenece a la clase.
    def convert_currency(value): #Se indicara que se recibira el cambio de dolares a pesos mexicanos.
        # Tipo de cambio fijo: 1 USD = 17.50 MXN
        pesos = value * 17.50
        print(f"${value} USD = ${pesos} MXN") #se imprimira el cambio de dolares a pesos mexicanos.
        return pesos #utilizaremos el return para devolver el valor a pesos mexicanos.

# Ejemplo de uso
cuenta1 = BankAccount("Juan", 500) #crearemos un objeto con el nombre de juan y un saldo de 500 dolares como ejemplo.

cuenta1.show_balance()          # método de instancia
BankAccount.show_bank()         # método de clase
BankAccount.convert_currency(100)  # método estático