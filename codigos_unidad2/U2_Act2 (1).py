class accountant: #crearemos la clase accountant
    def generate_report(self): #definiremos el metodo generate_report para generar un reporte financiero.
        print("Generating financial report") #se imprimira el mensaje de generacion del reporte financiero.

class technician: #se creara la clase technician para representar a un tecnico.
    def repair_machine(self): #definiremos el metodo repair_machine.
        print("Repairing machine") #se imprimira el mensaje de reparacion de la maquina.

class boss(accountant, technician): #En esta clase se heredara los atributos de las clases accountant y technician.
    pass #Deja la clase vacia, ya que no se agregaran nuevos atributos o metodos.

boss1 = boss() #crearemos un objeto de la clase boss.
boss1.generate_report() #llamamos al metodo generate_report de la clase accountant.
boss1.repair_machine() #llamamos al metodo repair_machine de la clase technician.