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
    #Rellenar una carga aleatoriamente
    def rellenar_carga(self, n):
        tipos_residuos = ["vidrio", "plastico", "papel", "metal", "organico", "otro"]
        for i in range(n):
            cantidad = random.randint(1, 20)
            tipo = random.choice(tipos_residuos)
            # Creo un objeto del tipo residuo con atributos aleatorios
            residuo = Residuo(cantidad, tipo)
            # Agrego el residuo a la carga
            self.add_residuos(residuo)

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
    def __init__(self):
        self.recorrido = []
    def add_punto_geografico(self, punto):
        self.recorrido.append(punto)
    def rellenar_ruta(self, lista_puntos):
        # Mezclar los puntos aleatoriamente
        random.shuffle(lista_puntos)
        # Llenar la ruta con 5 puntos aleatorios
        puntos_aleatorios = random.sample(lista_puntos, 5)
        # Recorrer la lista de puntos aleatorios
        for punto in puntos_aleatorios:
            self.add_punto_geografico(punto)
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

#========================================================================================
#Codigo Principal

#========================================================================================
#Importar libreria random
import random

#================================================================================================
#Creacion de los Puntos Geograficos
Punto1 = Punto_Geografico("A", 10, 20)
Punto2 = Punto_Geografico("B", 20, 30)
Punto3 = Punto_Geografico("C", 30, 40)
Punto4 = Punto_Geografico("D", 40, 50)
Punto5 = Punto_Geografico("E", 50, 60)
Punto6 = Punto_Geografico("F", 60, 70)
Punto7 = Punto_Geografico("G", 70, 80)
Punto8 = Punto_Geografico("H", 80, 90)
Punto9 = Punto_Geografico("I", 90, 100)
Punto10 = Punto_Geografico("J", 100, 110)
#Se agregan a una lista
Lista_puntos = [Punto1, Punto2, Punto3, Punto4, Punto5, Punto6, Punto7, Punto8, Punto9, Punto10]

#Creacion de las rutas
Ruta1 = Ruta()
Ruta2 = Ruta()
#Rellenar las rutas con puntos geograficos aleatorios
Ruta1.rellenar_ruta(Lista_puntos)
Ruta2.rellenar_ruta(Lista_puntos)

# Descripcion de las rutas
Ruta1.describir_ruta()

#========================================================================================
#Creacion de la empresa principal
TrashCity = TrashCity("TrashCity")

#Creacion de los camiones de la empresa
Camion1 = Camion(1, "Diurno")
Camion2 = Camion(2, "Nocturno")
Camion3 = Camion(3, "Diurno")

#Creacion de los conductores de la empresa
Conductor1 = Conductor("Juan", 30, "Hombre", 1)
Conductor2 = Conductor("Pedro", 40, "Hombre", 2)
Conductor3 = Conductor("Maria", 35, "Mujer", 3)

#Creacion de los recolectores de la empresa
Recolector1 = Recolector("Luis", 25, "Hombre", 11)
Recolector2 = Recolector("Ana", 30, "Mujer", 111)
Recolector3 = Recolector("Jose", 20, "Hombre", 22)
Recolector4 = Recolector("Sofia", 25, "Mujer", 222)
Recolector5 = Recolector("Carlos", 30, "Hombre", 33)
Recolector6 = Recolector("Laura", 20, "Mujer", 333)

#Creacion de los usuarios de la empresa
Usuario1 = Usuario("Juan", 30, "Hombre", 1, 1)
Usuario2 = Usuario("Pedro", 40, "Hombre", 2, 2)
Usuario3 = Usuario("Maria", 35, "Mujer", 3, 3)

#===================================================================================================

#Registro de los camiones en la empresa
TrashCity.add_camion(Camion1)
TrashCity.add_camion(Camion2)
TrashCity.add_camion(Camion3)

#Registro del personal en los camiones
Camion1.add_conductor(Conductor1)
Camion1.add_recolector(Recolector1, Recolector2)
Camion2.add_conductor(Conductor2)
Camion2.add_recolector(Recolector3, Recolector4)
Camion3.add_conductor(Conductor3)
Camion3.add_recolector(Recolector5, Recolector6)









