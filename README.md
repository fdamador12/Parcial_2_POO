# Parcial_2_POO

Estudiante: Franklin Amador Velasco
Codigo: 200180542


# Manual de Usuario - Sistema TrashCity

Bienvenido al sistema TrashCity, un sistema de gestión de recolección de residuos. Este manual proporciona una guía detallada sobre cómo utilizar el sistema y sus principales funcionalidades. Siga las instrucciones a continuación para comenzar a utilizar el sistema TrashCity.

1. Registro de la Empresa y el Centro de Acopio
  Al iniciar el sistema, se debe registrar el nombre de la empresa TrashCity y el nombre del centro de acopio mediante el código proporcionado.
  Una vez registrado, se mostrará un mensaje confirmando la creación de la empresa.
  
2. Creación de Puntos Geográficos y Rutas
  El siguiente paso es crear puntos geográficos que representen ubicaciones en la ciudad.
  Cada punto geográfico debe tener un nombre, una latitud y una longitud.
  Luego, se pueden crear rutas que consisten en una serie de puntos geográficos.
  Las rutas se rellenan automáticamente con puntos geográficos aleatorios de la lista creada.
  
3. Registro de Camiones y Personal
  Registre los camiones de recolección de basura en la empresa TrashCity.
  Cada camión debe tener un identificador único y especificar si es diurno o nocturno.
  Luego, registre el personal asociado a cada camión, incluyendo conductores y recolectores.
  Los conductores y recolectores deben proporcionar su nombre, edad, sexo e identificación única.
  
4. Asignación de Rutas, Camiones y Cargas
  Asigne las rutas, camiones y cargas a los turnos correspondientes.
  Cada turno debe tener un nombre, un identificador único, una ruta asignada, una carga de residuos y horarios de inicio y fin.
  Las cargas se llenan automáticamente con una cantidad aleatoria de residuos de diferentes tipos.
  
5. Realización de los Turnos
  Inicie los turnos y observe la información relevante.
  Durante la realización de un turno, se mostrará la información de la ruta, la carga de residuos y el camión responsable.
  También se indicarán los conductores y recolectores asociados a cada camión.
  Al finalizar un turno, se mostrará un mensaje de finalización.
  
6. Registro de Cuentas y Estadísticas en el Centro de Acopio
  Producir una cuenta para cada turno realizado en el centro de acopio.
  Las cuentas muestran la cantidad de residuos recolectados de cada tipo (vidrio, plástico, papel, metal, orgánico y otros).
  Las cuentas se agregan a una lista en el centro de acopio y se muestra la descripción de cada cuenta.
  Además, se registra la cantidad total de vidrio recolectado por el centro de acopio.
  
7. Notificaciones y Reportes
  El centro de acopio puede enviar notificaciones sobre la cantidad total de vidrio recolectado.
  También se pueden generar reportes adicionales según sea necesario.
  
8. Identificación de Personal y Funciones Adicionales
  Cada persona (conductores, recolectores) puede identificarse para mostrar su información personal.
  Además, se pueden realizar funciones adicionales según los requisitos del sistema.
 
9. Este manual de usuario proporciona una descripción general de las principales funcionalidades del sistema TrashCity. Siga las instrucciones y utilice los comandos proporcionados    en el código para interactuar con el sistema de manera efectiva.

# Explicacion UML

>A continuacion se señalará brevemente los factores mas importantes del diagrama UML del respectivo programa diseñado.
>1. La clase principal TrashCity contiene las rutas y los camiones de la empresa y puede rellenar estos
>2. La clase centro de acopio se encarga de organizar los residuos recogidos en cada turno respectivamente asi como calcular totales y la cantidad de vidrio recogida al finalizar el dia
>3. La clase camion tiene un id para identificarse asi como un conductor y 2 recolectores y el turno que realiza
>4. De la clase persona heredan recolector y conductor los cuales van dentro del camion al momento de realizar algun turno
>5. La clase turno tiene una ruta a seguir, una carga recolectada, un camion que la realiza y una fecha de inicio y finalizacion
>6. La clase carga tiene un cargamento con todos los residuos recolectados en un turno en particular
>7. La clase residuo muestra la cantidad y el tipo que se recolecta
>8. La clase ruta contiene un recorrido donde almacena puntos geograficos
>9. La clase puntos geograficos consta de un nombre para identificarse y de coordenadas de latitud y longitud
>-----------------------------------------------------------------------------------------------------------------------------------------------
Adjunto del UML: 
[Parcial_2_POO.pdf](https://github.com/fdamador12/Parcial_2_POO/files/11521489/Parcial_2_POO.pdf)

