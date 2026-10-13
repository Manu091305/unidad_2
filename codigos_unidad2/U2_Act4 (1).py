class Motor: #crearemos la clase motor para representar el motor de un auto.
    def arrancar(self): #definiremos el metodo arrancar para encender el motor.
        print("Motor encendido") #se encargara de imprimir el mensaje de que el motor esta encendido.

class Auto: #crearemos la clase auto para representar un automovil.
    def __init__(self, motor): #definiremos el metodo constructor con el atributo motor.
        self.motor = motor #se guardara el motor del auto.

    def arrancar_auto(self): #definiremos el metodo arrancar_auto para encender el auto.
        self.motor.arrancar() #se llamara al metodo arrancar del motor.

motor = Motor() #crearemos un objeto de la clase motor.
auto1 = Auto(motor) #crearemos un objeto de la clase auto y le pasaremos el objeto motor como parametro.
auto1.arrancar_auto() #se mandara a llamar el metodo arrancar_auto para encender el auto, lo que a su vez encendera el motor.
