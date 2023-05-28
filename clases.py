
import csv

class Vehículo:
    def __init__(self, marca, modelo, numeroruedas):
        self.marca = marca
        self.modelo = modelo
        self.numeroruedas = numeroruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos_csv", "a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print("El Archivo csv no se ha creado")
    
    def leer_datos_csv(self):
        try:
            with open("vehiculos_csv", "r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de Vehículos {type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item [0]:
                        print(item[1])
                        print("")
        except:
            pass
                
    def __str__ (self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numeroruedas} ruedas"

class Automóvil(Vehículo):
    def __init__(self, marca, modelo, numeroruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numeroruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def __str__ (self):
    return Vehículo.__str__(self) + f"{self.velocidad}, {self.cilindrada} cc,"

class Particular (Automóvil):
    def __init__(self, marca, modelo, numeroruedas, velocidad, cilindrada, numeropuesto):
        super().__init__(marca, modelo, numeroruedas, velocidad, cilindrada)
        self.numeropuesto = numeropuesto

    def get_numeropuesto (self):
        return self.numeropuesto
    
    def set_numeropuesto (self, numeropuesto_new):
        self.numeropuesto = numeropuesto_new

    def __str__ (self):
        return Automóvil.__str__(self) + f" Puestos: {self.numeropuesto}"

class Carga (Automóvil):
    def __init__(self, marca, modelo, numeroruedas, velocidad, cilindrada, peso):
        super().__init__(marca, modelo, numeroruedas, velocidad, cilindrada)
        self.peso = peso
    
    def __str__ (self):
        return Automóvil.__str__(self) + f" Carga: {self.peso}"   

class Bicicleta (Vehículo):
    def __init__(self, marca, modelo, numeroruedas, tipo):
        super().__init__(marca, modelo, numeroruedas)
        self.tipo = tipo
    
    def __str__ (self):
        return Vehículo.__str__(self) + f" Tipo: {self.tipo}"

class Motocicleta (Bicicleta):
    def __init__(self, marca, modelo, numeroruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numeroruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__ (self):
        return Bicicleta.__str__(self) + f" Radios: {self.nro_radios} , Cuadro: {self.cuadro}, Motor: {self.motor}"



