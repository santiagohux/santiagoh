class Recurso:
    def __init__(self, nombre, capacidad_total, unidad):
        self.nombre = nombre
        self.capacidad_total = capacidad_total
        self.disponible = capacidad_total
        self.unidad = unidad
        self.uso = 0

    def asignar(self, cantidad):
        if cantidad <= self.disponible:
              self.disponible -= cantidad
              self.actualizar_uso()
              return True
        else:
              return False
        
    def liberar(self, cantidad):
         self.disponible += cantidad
         self.actualizar_uso()

    def actualizar_uso(self):
         self.uso = ((self.capacidad_total - self.disponible) / self.capacidad_total) * 100


    def __str__(self):
        return f"Recurso: {self.nombre}, Capacidad Total: {self.disponible} {self.unidad}, Uso: {self.uso}%"
    
class CPU(Recurso):
    def __init__(self, capacidad_total = 100):
        super().__init__("CPU", capacidad_total, "%")

class RAM(Recurso):
    def __init__(self, capacidad_total):
        super().__init__("RAM", capacidad_total, "MB")

class Disco(Recurso):
    def __init__(self, capacidad_total):
        super().__init__("Disco", capacidad_total, "GB")


class Proceso():
    def __init__(self, nombre, requiere_cpu = 0, requiere_ram = 0, requiere_disco = 0):
        self.nombre = nombre
        self.estado = 'Listo'
        self.requiere_cpu = requiere_cpu
        self.requiere_ram = requiere_ram
        self.requiere_disco = requiere_disco
        self.recursos_asignados = {
            'cpu' : 0,
            'ram' : 0,
            'disco' : 0
        }


    def __str__(self):
        return (f"Proceso: {self.nombre} ({self.estado})\n"
                f"Requiere:\n"
                f"CPU: {self.requiere_cpu} %\n"
                f"RAM: {self.requiere_ram} MB\n"
                f"Disco: {self.requiere_disco} GB\n"
                f"Recursos Asignados:\n"
                f"CPU: {self.recursos_asignados['cpu']} %\n"
                f"RAM: {self.recursos_asignados['ram']} MB\n"
                f"Disco: {self.recursos_asignados['disco']} GB\n")

class SistemaOperativo():
    def __init__(self):
        self.procesos = []
        self.recursos = {
            'cpu': CPU(),
            'ram': RAM(2048),
            'disco': Disco(500)
        }

    def agregar_proceso(self, nombre, requiere_cpu, requiere_ram, requiere_disco):
        proceso= Proceso(nombre, requiere_cpu, requiere_ram, requiere_disco)
        #Aquí tengo que ir a preguntarle al método asignar recursos si se pueden asignar los recursos al proceso
        print ("Aquí se crean procesos")

    def asignar_recursos(self, proceso):
        print("Aquí se asignan recursos a los procesos")
        ##Aquí se asignan los recursos al proceso
        ##Tengo que hacer un if para ver si se pueden asignar los recursos al proceso

    def mostrar_recursos(self):
        print ("Aquí se muestran los recursos del sistema operativo")

    def mostrar_procesos(self):
        print ("Aquí se muestran los procesos del sistema operativo")

    def finalizar_proceso(self, proceso):
        print ("Aquí se finalizan los procesos del sistema operativo")
        if (self.recursos['cpu'].asignar(proceso.requiere_cpu) and
            self.recursos['ram'].asignar(proceso.requiere_ram) and
            self.recursos['disco'].asignar(proceso.requiere_disco)):
                proceso.estado = 'Ejecutando'
                proceso.recursos_asignados['cpu'] = proceso.requiere_cpu
                proceso.recursos_asignados['ram'] = proceso.requiere_ram
                proceso.recursos_asignados['disco'] = proceso.requiere_disco
                return True
        else:
            return False
       

    
if __name__ == "__main__":
    cpu = CPU()
    print(cpu)

    ram = RAM(2048)
    print(ram)

    disco = Disco(500)
    print(disco)

    cpu.asignar(20)
    ram.asignar(512)
    disco.asignar(1)
    print ('-------------------------------------------------')
    print(cpu)
    print(ram)
    print(disco)