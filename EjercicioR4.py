'''
Created on 16 may. 2022
@author: Juan Jaime Fuentes Uriarte
Agro-Sinaloa SA de CV es una empresa dedicada a la comercializaci�n de productos agr�colas a nivel nacional. 
Despu�s de una minuciosa evaluaci�n en sus procesos, la empresa ha decidido asignarte la tarea de desarrollar 
un programa en Python que les permita gestionar de una manera m�s eficiente las ventas por caja de sus principales 
productos: ma�z, grano, pepino y tomate verde.

Instrucciones:
El programa deber� solicitarle al responsable del almac�n de distribuci�n ingresar la siguiente informaci�n: cantidad de
 cajas a vender y el tipo de producto por ID (Ver tabla 1). Posterior a esto, el programa deber� mostrar como salida, el
nombre del producto que se seleccion�, el precio unitario por caja para ese producto y el monto total de la venta, teniendo
en cuenta un costo de env�o de $1,500 pesos, siempre y cuando la cantidad de cajas a vender sea menor o igual a 100 unidades.
'''
#Declaración de Variables del programa 
BdProductos = [[1,"Maíz grano",285.55],[2,"Pepino",334.72],[3,"Tomate verde",129.00]]
CostoEnvio = float(1500.00)

NumeroCajas = input("Número de cajas a vender: ")
IdProducto = input("ID del producto: ")

#for Interactor in BdProductos:
for cont in range(0, len(BdProductos)):
    Producto = BdProductos[cont]
    if ((int(Producto[0])==int(IdProducto)) and (int(NumeroCajas)<=150) ):
        NombreProducto = Producto[1]
        PrecioCaja = float(Producto[2])
        CostoTotal = (PrecioCaja * float(NumeroCajas))+CostoEnvio
        print ("El producto es: "+ NombreProducto)
        print ("El precio por caja es: "+ str(PrecioCaja))
        print ("El costo total a pagar: "+ str(CostoTotal))