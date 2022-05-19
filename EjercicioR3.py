'''
Creado on 13 may. 2022
@author: Juan Jaime Fuentes Uriarte
Planteamiento: 
ConstrucArgo SA de CV es una empresa dedicada a la venta de materiales de construcción ubicada en el Parque 
Industrial El Trébol, desde el cual envía a sus clientes del sector inmobiliario costales de cemento y yeso. Actualmente, 
ConstrucArgo cuenta con camiones que tienen la capacidad de transportar un máximo de 3,254 kg de carga cada uno, sin embargo, 
a fin de eficientizar costos de traslado y mantenimiento, el director de logística ha solicitado que no puedan realizarse 
entregas de materiales cuyo peso total sea menor al 50% de la capacidad de carga del camión ni cuyo peso exceda la capacidad
máxima.
Instrucciones:
En este sentido, el director de logística de la empresa te solicita un programa en Python que les permita saber si se podrá
realizar o no la entrega de un pedido según las restricciones anteriores y el número de costales de cemento y yeso que fueron 
requeridos por el cliente.
'''
BultoCemento = int(40)
BultoYeso = int(30)

CantidadCemento = input('Número de costales de cemento (kg): ')
CantidadYeso = input('Número de costales de yeso (kg):  ')

if int(CantidadCemento) > 0:
    PesoCemento = BultoCemento * int(CantidadCemento)  
if int(CantidadYeso) > 0:
    PesoYeso = BultoYeso * int(CantidadYeso)
      
TotalCarga = PesoCemento + PesoYeso

if ((TotalCarga <= 3254) and (TotalCarga >=1627)):
    print("El peso total en kg es: " + str(TotalCarga))
    print("¿Se puede realizar el envío?: True")
else:
    print("El peso total en kg es: " + str(TotalCarga))
    print("¿Se puede realizar el envío?: False")