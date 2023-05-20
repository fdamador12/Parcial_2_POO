#========================================================================================
#Clase Trashcity
class TrashCity:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, nombre):
        self.nombre = nombre
        self.rutas = []
        self.camiones = []
    def add_ruta(self, ruta):
        self.rutas.append(ruta)
    def add_camion(self, camion):
        self.camiones.append(camion)
    def rellenar_rutas(self, lista_rutas):
        for ruta in lista_rutas:
            self.add_ruta(ruta)
    def rellenar_camiones(self, lista_camiones):
        for camion in lista_camiones:
            self.add_camion(camion)

#========================================================================================
#Clase Centro de Acopio
class Centro_Acopio:
    _instance = None
    def __new__(cls, nombre):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []
        self.vidrio_total = 0
    def producir_cuenta(self, turno):
        # Crear una cuenta vacia
        cuenta = Cuenta(turno.id, 0, 0, 0, 0, 0, 0)
        # Recorrer la carga del camion
        for residuo in turno.carga.cargamento:
            if residuo.tipo == "vidrio":
                cuenta.cantidad_vidrio += residuo.cantidad
            elif residuo.tipo == "plastico":
                cuenta.cantidad_plastico += residuo.cantidad
            elif residuo.tipo == "papel":
                cuenta.cantidad_papel += residuo.cantidad
            elif residuo.tipo == "metal":
                cuenta.cantidad_metal += residuo.cantidad
            elif residuo.tipo == "organico":
                cuenta.cantidad_organico += residuo.cantidad
            else:
                cuenta.cantidad_otro += residuo.cantidad
        # Agregar la cuenta a la lista de cuentas del centro de acopio
        self.cuentas.append(cuenta)
        # Modificar el vidrio total de todas las rutas
        self.modificar_vidrio_total(cuenta.cantidad_vidrio)
    def describir_cuenta(self, turno):
        for cuenta in self.cuentas:
            if cuenta.id == turno.id:
                print(f"\nLa cuenta del camion no. {cuenta.id} informa de: ")
                print(f"  Cantidad de vidrio: {cuenta.cantidad_vidrio}")
                print(f"  Cantidad de plastico: {cuenta.cantidad_plastico}")
                print(f"  Cantidad de papel: {cuenta.cantidad_papel}")
                print(f"  Cantidad de metal: {cuenta.cantidad_metal}")
                print(f"  Cantidad de organico: {cuenta.cantidad_organico}")
                print(f"  Cantidad de otro: {cuenta.cantidad_otro}")
                print(f"  Total: {cuenta.calcular_total()}")
    def modificar_vidrio_total(self, monto):
        self.vidrio_total += monto
    def notificar_vidrio_total(self):
        print(f"\nEl centro de acopio {self.nombre} informa que recolectó {self.vidrio_total} kg de vidrio el dia de hoy")

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
#Clase Turno
class Turno:
    def __init__(self,nombre, id, ruta, carga, hora_inicio, hora_fin, camion):
        self.nombre = nombre
        self.id = id
        self.ruta = ruta
        self.carga = carga
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.camion = camion
    def realizar_turno(self):
        print(f"\n{self.nombre} esta en proceso, no. {self.id}")
        print(f"Hora de inicio: {self.hora_inicio}  - Hora de fin: {self.hora_fin}")
        print(f"{self.ruta.describir_ruta()}")
        print(f"El cargamento encontrado fue:")
        for residuo in self.carga.cargamento:
            print(f"  Tipo: {residuo.tipo}, Cantidad: {residuo.cantidad}")
        print(f"Id camion: {self.camion.id}. Responsables: {self.camion.conductor.nombre}, {self.camion.recolectorA.nombre} y {self.camion.recolectorB.nombre}")

#========================================================================================
#Clase Carga
class Carga:
    def __init__(self, id):
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
        print(f"  Punto {self.nombre}. Latitud: {self.latitud}, longitud: {self.longitud}")

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
        # Llenar la ruta con n puntos aleatorios (5 - 10)
        puntos_aleatorios = random.sample(lista_puntos, random.randint(5, 10))
        # Recorrer la lista de puntos aleatorios
        for punto in puntos_aleatorios:
            self.add_punto_geografico(punto)
    def describir_ruta(self):
        print("La ruta es: ")
        for punto in self.recorrido:
            punto.describir_punto()

#========================================================================================
#Codigo Principal

#----------------------------------------------------------------------------------------
#Importar libreria random y unittest
import random
import unittest
from unittest.mock import MagicMock

#----------------------------------------------------------------------------------------
#Creacion de la empresa principal
TrashCity = TrashCity("TrashCity")
print(f"       ====|La empresa {TrashCity.nombre} ha sido creada|====")
#Creacion del centro de acopio
Centro_Acopio = Centro_Acopio("Centro de Acopio")

#----------------------------------------------------------------------------------------
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
#Son agregados a una lista
Lista_puntos = [Punto1, Punto2, Punto3, Punto4, Punto5, Punto6, Punto7, Punto8, Punto9, Punto10]

#----------------------------------------------------------------------------------------
#Creacion de las rutas
Ruta1 = Ruta()
Ruta2 = Ruta()
Ruta3 = Ruta()
#Rellenar las rutas con puntos geograficos aleatorios
Ruta1.rellenar_ruta(Lista_puntos)
Ruta2.rellenar_ruta(Lista_puntos)
Ruta3.rellenar_ruta(Lista_puntos)
# Descripcion de las rutas
Ruta1.describir_ruta()
Ruta2.describir_ruta()
Ruta3.describir_ruta()

#----------------------------------------------------------------------------------------
#Creacion de los camiones de la empresa
Camion1 = Camion(1, "Diurno")
Camion2 = Camion(2, "Nocturno")
Camion3 = Camion(3, "Diurno")
#Creacion de los conductores de la empresa
Conductor1 = Conductor("Marcela", 30, "Mujer", 1)
Conductor2 = Conductor("Pedro", 40, "Hombre", 2)
Conductor3 = Conductor("Maria", 35, "Mujer", 3)
#Creacion de los recolectores de la empresa
Recolector1 = Recolector("Luis", 25, "Hombre", 11)
Recolector2 = Recolector("Ana", 30, "Mujer", 111)
Recolector3 = Recolector("Jose", 20, "Hombre", 22)
Recolector4 = Recolector("Sofia", 25, "Mujer", 222)
Recolector5 = Recolector("Carlos", 30, "Hombre", 33)
Recolector6 = Recolector("Laura", 20, "Mujer", 333)

#----------------------------------------------------------------------------------------
#Registro de los camiones y rutas en la empresa
Lista_camiones = [Camion1, Camion2, Camion3]
Lista_rutas = [Ruta1, Ruta2, Ruta3]
#Rellenar informacion de los camiones y rutas
TrashCity.rellenar_camiones(Lista_camiones)
TrashCity.rellenar_rutas(Lista_rutas)

#----------------------------------------------------------------------------------------
#Registro del personal en los camiones
Camion1.add_conductor(Conductor1)
Camion1.add_recolector(Recolector1, Recolector2)
Camion2.add_conductor(Conductor2)
Camion2.add_recolector(Recolector3, Recolector4)
Camion3.add_conductor(Conductor3)
Camion3.add_recolector(Recolector5, Recolector6)

#----------------------------------------------------------------------------------------
#Creacion de las cargas y rellenarlas con n residuos aleatorios (5-10)
Carga1 = Carga(999)
Carga2 = Carga(222)
Carga3 = Carga(333)
Carga1.rellenar_carga(random.randint(5, 10))
Carga2.rellenar_carga(random.randint(5, 10))
Carga3.rellenar_carga(random.randint(5, 10))

#----------------------------------------------------------------------------------------
#Creacion de los turnos
Turno1 = Turno("Turno Diurno", 444, Ruta1, Carga1, "6:00", "18:00", Camion1)
Turno2 = Turno("Turno Nocturno", 777, Ruta2, Carga2, "18:00", "4:00", Camion2)
Turno3 = Turno("Turno Diurno", 555, Ruta3, Carga3, "6:00", "18:00", Camion3)
#Realizar los turnos
Turno1.realizar_turno()
Turno2.realizar_turno()
Turno3.realizar_turno()

#----------------------------------------------------------------------------------------
#Crear las cuentas en el centro de acopio
Centro_Acopio.producir_cuenta(Turno1)
Centro_Acopio.producir_cuenta(Turno2)
Centro_Acopio.producir_cuenta(Turno3)
#Mostrar las cuentas del centro de acopio
Centro_Acopio.describir_cuenta(Turno1)
Centro_Acopio.describir_cuenta(Turno2)
Centro_Acopio.describir_cuenta(Turno3)
#Notificar el total de vidrio recolectado en todos los turnos
Centro_Acopio.notificar_vidrio_total()

#================================================================================================
#Pruebas Unitarias

class TestPersona(unittest.TestCase):
    def test_identificarse(self):
        persona = Persona("Juan", 25, "Hombre")
        self.assertEqual(persona.identificarse(), "Hola, soy Juan, soy Hombre y tengo 25 años")

class TestConductor(unittest.TestCase):
    def test_conducir(self):
        conductor = Conductor("Pedro", 35, "Hombre", 123)
        camion = Camion(1, "Diurno")
        camion.add_conductor(conductor)
        self.assertEqual(conductor.conducir(camion), "El conductor Pedro está conduciendo el camion no. 1")

class TestRecolector(unittest.TestCase):
    def test_recolectar(self):
        recolector = Recolector("María", 28, "Mujer", 456)
        camion = Camion(2, "Nocturno")
        camion.add_recolector(recolector, None)
        self.assertEqual(recolector.recolectar(camion), "El recolector María está recolectando basura en el camion no. 2")

class TestCarga(unittest.TestCase):
    def test_rellenar_carga(self):
        carga = Carga(999)
        residuo1 = Residuo(5, "papel")
        residuo2 = Residuo(10, "vidrio")
        carga.add_residuos(residuo1)
        carga.add_residuos(residuo2)
        carga.rellenar_carga(3)
        self.assertEqual(len(carga.residuos), 5)  # La carga debería tener 5 residuos en total

class TestTrashCity(unittest.TestCase):
    def setUp(self):
        self.trash_city = TrashCity("TrashCity")

    def test_singleton_instance(self):
        trash_city2 = TrashCity("AnotherTrashCity")
        self.assertEqual(self.trash_city, trash_city2)

    def test_add_ruta(self):
        ruta = MagicMock()
        self.trash_city.add_ruta(ruta)
        self.assertIn(ruta, self.trash_city.rutas)

class TestCuenta(unittest.TestCase):
    def setUp(self):
        self.cuenta = Cuenta(1, 10, 20, 30, 40, 50, 60)

    def test_calcular_total(self):
        total = self.cuenta.calcular_total()
        self.assertEqual(total, 210)

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.turno = Turno("Turno 1", 1, None, None, "9:00", "17:00", None)

    def test_realizar_turno(self):
        pass

class TestResiduo(unittest.TestCase):
    def setUp(self):
        self.residuo = Residuo(5, "vidrio")

    def test_constructor(self):
        self.assertEqual(self.residuo.cantidad, 5)
        self.assertEqual(self.residuo.tipo, "vidrio")

if __name__ == "__main__":
    unittest.main()




