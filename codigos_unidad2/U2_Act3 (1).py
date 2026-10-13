# Polimorfismo: Un metodo puede comportarse de diferentes maneras dependiendo del objeto que lo utilice.

# Clase para empleados de tiempo completo
class FulltimeEmployee:
    def __init__(self, name, salary): #se definira el metodo constructor con los atributos de name y salary.
        self.name = name #se guardara el nombre del empleado.
        self.salary = salary #se guardara el salario del empleado.
    
    def payment(self): #aqui se mostrara el pago del empleado de tiempo completo.
        return f"{self.name} recibe un pago fijo de {self.salary}." #se regresara el nombre del empleado y su pago fijo.

# Clase para empleados por hora
class HourlyEmployee:
    def __init__(self, name, hours_worked, hourly_rate): #se definira el metodo constructor con los atributos de name, hours_worked y hourly_rate.
        self.name = name #se guardara el nombre del empleado.
        self.hours_worked = hours_worked #se guardara la cantidad de horas trabajadas.
        self.hourly_rate = hourly_rate #se guardara la tarifa horaria.

    def payment(self): #aqui se mostrara el pago del empleado por hora.
        total = self.hours_worked * self.hourly_rate #se calculara el pago total multiplicando las horas trabajadas por la tarifa de hora.
        return f"{self.name} recibe un pago por horas de {total}." #se regresara el nombre del empleado y su pago por horas.

# Función que usa polimorfismo
def calculate_payment(worker): #se definira la funcion calculate_payment que recibira un objeto worker.
    print(worker.payment()) #se mandara a llamar al metodo payment del objeto worker, que puede ser de tipo FulltimeEmployee o HourlyEmployee.

# Probando con diferentes objetos
emp1 = FulltimeEmployee("Rocio", 5000) #se creara un objeto con el nombre de rocio y un salario de 5000.
emp2 = HourlyEmployee("Luis", 40, 100) #se creara un objeto con el nombre de luis, 40 horas trabajadas y una tarifa de 100 por hora.

calculate_payment(emp1)  # Llama al método payment de FulltimeEmployee 
calculate_payment(emp2)  # Llama al método payment de HourlyEmployee
