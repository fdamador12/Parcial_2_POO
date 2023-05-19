#========================================================================================
#Clase Trashcity
class TrashCity:
    def __init__(self, nombre):
        self.nombre = nombre
        self.rutas = []
        self.camiones = []
    def add_ruta(self, ruta):
        self.rutas.append(ruta)
    def add_camion(self, camion):
        self.camiones.append(camion)

#========================================================================================
#Clase Camion
class Camion:
    def __init__(self, id, turno):
        self.id = id
        self.turno = turno
    def add_conductor(self, conductor):
        self.conductor = conductor
    def add_recolector(self, recolectorA, recolectorB):
        self.recolectorA = recolectorA
        self.recolectorB = recolectorB
    def realizar_turno(self):
        pass

#========================================================================================
#Clase Persona
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    def identificarse(self):
        print(f"Hola, soy {self.nombre}, soy {self.sexo} y tengo {str(self.edad)} años")

#========================================================================================
#Clase Conductor
class Conductor(Persona):
    def __init__(self, nombre, edad, sexo, id):
        super().__init__(nombre, edad, sexo)
        self.id = id
    def conducir(self, camion):
        print(f"El conductor {self.nombre} está conduciendo el camion no. {camion.id}")

#========================================================================================
#Clase Recolector
class Recolector(Persona):
    def __init__(self, nombre, edad, sexo, id):
        super().__init__(nombre, edad, sexo)
        self.id = id
    def recolectar(self, camion):
        print(f"El recolector {self.nombre} está recolectando basura en el camion no. {camion.id}")

#========================================================================================
#Clase Usuario
class Usuario(Persona):
    def __init__(self, nombre, edad, sexo, pos_lat, pos_long):
        super().__init__(nombre, edad, sexo)
        self.posicion_latitud = pos_lat
        self.posicion_longitud = pos_long
    def arrojar_desechos(self, ruta):
        print(f"El usuario {self.nombre} está arrojando desechos en ...")

#========================================================================================
#Clase Turno
class Turno:
    def __init__(self,nombre, id, ruta, carga, hora_inicio, hora_fin):
        self.nombre = nombre
        self.id = id
        self.ruta = ruta
        self.carga = carga
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

#========================================================================================
#Clase Carga
class Carga:
    def __init__(self, id, cargamento):
        self.id = id
        self.cargamento = []
    def add_residuos(self, residuo):
        self.cargamento.append(residuo)

#========================================================================================
#Clase Residuo
class Residuo:
    def __init__(self, cant, tipo):
        self.cantidad = cant
        self.tipo = tipo
#========================================================================================
#Clase Punto Geografico
class Punto_Geografico:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
    def describir_punto(self):
        print(f"El punto {self.nombre} está en la latitud {self.latitud} y longitud {self.longitud}")

#========================================================================================
#Clase Ruta
class Ruta:
    def __init__(self, recorrido):
        self.recorrido = []
    def add_punto_geografico(self, punto):
        self.recorrido.append(punto)
    def describir_ruta(self):
        print("La ruta es: ")
        for punto in self.recorrido:
            punto.describir_punto()

#========================================================================================
#Clase Centro de Acopio
class Centro_Acopio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.camiones = []
    def producir_cuenta(self, camion):
        pass
    def describir_total(self):
        pass

#========================================================================================
#Clase Cuenta
class Cuenta:
    def __init__(self, id_turno, cantV, cantP, cantPL, cantM, cantO, cantOT):
        self.id = id_turno
        self.cantidad_vidrio = cantV
        self.cantidad_plastico = cantP
        self.cantidad_papel = cantPL
        self.cantidad_metal = cantM
        self.cantidad_organico = cantO
        self.cantidad_otro = cantOT
    def calcular_total(self):
        return self.cantidad_vidrio + self.cantidad_plastico + self.cantidad_papel + self.cantidad_metal + self.cantidad_organico + self.cantidad_otro












