class Personas:
    def __init__(self, nombre, apellido, dni):
        self.nombre = []
        self.apellido = []
        self.dni = []
    
    def __del__(self):
        pass

    def menu(self):
        opcion = 0
        while opcion != 6:
            print("1. AGREGAR REGISTRO")
            print("2. ELIMINAR REGISTRO")
            print("3. BUSCAR REGISTRO")
            print("4. ORDENAR ARCHIVO POR")
            print("5. MOSTRAR ARCHIVO")
            print("6. SALIR")
            opcion = int(input("Ingrese el valor de la opción: "))
            match opcion:
                case 1:
                    self.agregarRegistro()
                case 2:
                    self.eliminarRegistro()
                case 3:
                    self.buscarRegistro()
                case 4:
                    self.ordenarArchivo()
                case 5:
                    self.mostrarArchivo()
                case 6:
                    self.finalizar()
                case _:
                    print("Error. Opción fuera de rango. ")
                
        def cargarRegistro(self) -> dict:
            archivo = open("/Users/tomasprodan/Documents/Info GRAL/Practica 7/7.7/7.7personas.csv", "r")
            dic = {}
            for linea in archivo:
                linea = linea.split(",")
                dic[int(linea[2])]=[linea[0],linea[1]]
            archivo.close()
            return dic
            
        def agregarRegistro(self, dni, nombre,):
            dic = cargarRegistro()
            dni = int(input("Ingrese DNI: "))
            if dni in self.cargarRegistro():
                dni = int(input("ERROR. DNI ya existe."))
            pass

            # if opcion == 1: self.cargarRegistro()
            # elif opcion == 2: self.eliminarRegistro()
            # elif opcion == 3: self.