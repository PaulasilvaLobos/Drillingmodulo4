from clases import Vehículo, Automóvil

instancias = []
n =int(input("Cuantos vehículos desea insertar:"))

for i in range (n):
    print (f"Datos del automovil {i+1}")
    marca = input("inserte la marca del automovil: ")
    modelo = input("inserte el modelo del automovil: ")
    numeroruedas = input("inserte el número de ruedas del automovil: ")
    velocidad = input("inserte velocidad del automovil expresado en KM/H: ")
    cilindrada = input("ingrese la cilindrada del automovil en CC: ")
    print("")
    auto = Automóvil(marca, modelo, numeroruedas, velocidad, cilindrada)
    instancias.append(auto)

print("Imprimir por pantalla los vehículos")

for index, item in enumerate(instancias):
    print(f"Datos del automovil {index+1} : Marca del automovil {item.marca}, Modelo del automovil {item.modelo}, Número de ruedas del automovil {item.numeroruedas}, Velocidad en KM/H {item.velocidad}, Cilindraje {item.cilindrada} cc") 

