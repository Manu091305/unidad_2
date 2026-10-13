class person: #se creara la clase person para representar a una persona.
    def __init__(self, name, age, city): #se creara un metodo constructor con los atributos de name, age y city.
        self.name = name #se guardara el nombre de la persona.
        self.age = age #se guardara la edad de la persona.
        self.city = city#se guardara la ciudad de la persona.

    def greet(self): #Crearemos un metodo llamado greet.
        print(f"Hi, mi name is {self.name}, I am {self.age} years old, and I lived in {self.city}.") #Aqui se mostraran los atributos de la persona.

person1 = person("Juan", 15, "Guadalajara") #Le asignaremos los atributos juan, 15 y guadalajara.
person2 = person("Maria", 22, "Tijuana") #Le asignaremos los atributos maria, 22 y tijuana.
person3 = person("Mateo", 18, "Culiacan") #Le asignaremos los atributos mateo, 18 y culiacan.

person1.greet() #se mandara a llamar el metodo greet para mostrar la informacion de la persona 1.
person2.greet() #se mandara a llamar el metodo greet para mostrar la informacion de la persona 2.
person3.greet() #se mandara a llamar el metodo greet para mostrar la informacion de la persona 3.