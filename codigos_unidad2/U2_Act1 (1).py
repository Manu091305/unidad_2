class employee: #crearemos la clase employee
    def __init__(self, name, salary):#definiremos el metodo constructor con los atributos de name y salary.
        self.name = name #se guardara el nombre del empleado.
        self.salary = salary #se guardara el salario del empleado.

    def show_info(self): #aqui se mostrara la informacion del empleado.
        print(f"Name: {self.name}, Salary: {self.salary}") #se imprimira el nombre y salario del empleado.

class manager(employee): #crearemos la clase manager que heredara los atributos de la clase employee.
    def __init__(self, name, salary, department): #definiremos el metodo constructor con los atributos de name, salary y department.
        super().__init__(name, salary, department) # Con este super mandaremos a llamar al metodo constructor de la clase padre.
        self.department = department #se guardara el departamento del manager.

    def show_info(self):#aqui mostraremos la informacion del manager.
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}") #se imprimira el nombre, salario y departamento del manager.

manager1 = manager("Laura", 60000, "Networking") #crearemos un objeto con el nombre de laura, un salario de 60000 y el departamento de networking como ejemplo.
manager1.show_info() #se mandara a llamar el metodo show_info para mostrar la informacion del manager.