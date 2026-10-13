class car: #se creara la clase car para representar un automovil.
    def __init__(self, brand, model, color): #Crearemos un metodo contructor el cual tendra los atributos de la marca, modelo y color.
        self.brand = brand #se guardara la marca del automovil.
        self.model = model #se guardara el modelo del automovil.
        self.color = color #se guardara el color del automovil.

    def show_info(self): #Con el metodo show_info se mostrara la informacion del automovil.
        print(f"brand: {self.brand}, model: {self.model}, color: {self.color}") #En este apartado se mostraran los atributos del automovil.
#se creara el primer onjeto de la clase car.
car1 = car("Chevrolet", "Suburban", "Blanco") #le asignaremos los atributos chevrolet, suburban y blanco.
#se creara el segundo objeto de la clase car.
car2 = car("Toyota", "Tacoma", "Azul") #le asignaremos los atributos toyota, tacoma y azul.

car1.show_info() #Aqui se mandara a llamar el metodo show_info para mostrar la informacion del automovil 1.
car2.show_info() #Aqui se mandara a llamar el metodo show_info para mostrar la informacion del automovil 2.