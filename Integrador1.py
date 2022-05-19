'''
Creado on 13 may. 2022
@author: Juan Jaime Fuentes Uriarte
Planteamiento: 
Gracias a los buenos resultados que obtuvo la empresa Agro-Sinaloa SA de CV con 
la implementaci�n del programa anterior (Ejercicio retador #4 ) han decidido solicitar
tu ayuda para agregar una nueva funcionalidad que les permita reducir la merma de sus
productos ofreciendo un descuento del 20% al total de la compra siempre que las ventas 
durante el d�a sean menores a 1500 cajas.

Instrucciones:
Tomando como base el programa desarrollado en el ejercicio anterior, agrega directamente en tu
 c�digo la siguiente lista ventas_productos que contiene la relaci�n de ventas que se han 
 realizado por cada uno de los productos durante el d�a: 
 venta_productos = [ [2, 122], [1, 89], [1, 22], [3, 48], [1, 75], [3, 322], [2, 95], [1, 148], [1, 83], [3, 100] ] 
 El primer valor de cada sublista hace referencia al ID del producto, y el segundo a la cantidad
  de cajas que se vendieron durante esa compra, es decir: [ID_producto, cajas_vendidas]. 
  Con esto en cuenta, ahora el programa deber� mostrar como salida, el nombre del producto 
  que se seleccion�, el precio unitario por caja para ese producto, si aplica o no el 
  descuento del 20% seg�n la suma de ventas acorde a la lista ventas_productos y el monto 
  total de la venta contemplando el costo de env�o de $1,500 pesos siempre y 
  cuando la cantidad de cajas a vender sea menor o igual a 100 unidades m�s y el descuento
   si las ventas totales superan las 1500 cajas.
'''
#Declaraci�n de Variables del programa 
BdProductos = [[1,"Maíz grano",285.55],[2,"Pepino",334.72],[3,"Tomate verde",129.00]]
AcumuladoVentasDia= int(0)
venta_productos = [[2,122],[1,89],[1,22],[3,48],[1,75],[3,322],[2,95],[1,148],[1,83],[3,100]]
NumeroCajas = input("Número de cajas a vender: ")
IdProducto = input("ID del producto: ")

#Calculo del costo de envioa apartir de la caontidad de cajas solicitadas 
if int(NumeroCajas) > 100:
    CostoEnvio = float(0)  
if int(NumeroCajas) <= 100:
    CostoEnvio = float(1500.00)

#Calculo de la cantidad de cajas registradas en las ventas
for InterVentas in range(0,len(venta_productos)):
    Venta = venta_productos[InterVentas]
    AcumuladoVentasDia += int(Venta[1]) 
                       

for cont in range(0, len(BdProductos)):   
    Producto = BdProductos[cont]
        
    if int(Producto[0])==int(IdProducto):
        NombreProducto = Producto[1]
        PrecioCaja = float(Producto[2])
        CostoTotal=(PrecioCaja * float(NumeroCajas))
        CostoTotal += CostoEnvio
            
        if (AcumuladoVentasDia + int(NumeroCajas))>1500:  
            CostoTotal = CostoTotal*.80
            Descuento= True
        else:
            Descuento =False
           
print ("El producto es: "+ NombreProducto)
print ("El precio por caja es: "+ str(PrecioCaja))
print ("Aplica descuento del 20%: "+ str(Descuento))
print ("El costo total a pagar: "+ str(int(CostoTotal)))   