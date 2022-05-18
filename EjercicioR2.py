'''
Creado on 13 may. 2022
@author: Juan Jaime Fuentes Uriarte
Planteamiento: Con el objetivo de mejorar el c�digo anterior (ejercicio retador, #1), 
la Secretar�a de Econom�a del estado de Sinaloa te solicita automatizar la tarea de 
creaci�n y asignaci�n de variables haciendo uso de la funci�n input para poder crear 
una lista que contenga la relaci�n municipio-n�mero de habitantes.
Esta lista deber� permitir obtener la sumatoria y el promedio de habitantes  de 
los municipios ingresados por el director de la Secretar�a cada vez que se ejecute
la nueva versi�n de tu programa.

Instrucciones: Para lograrlo, deber�s crear un nuevo programa en Python que cumpla 
con las siguientes caracter�sticas: 

1.- Solicitar al usuario que ingrese el nombre del municipio y agregarlo a una lista
llamada �municipios�. (Repetir este paso para aceptar 3 municipios diferentes).

2.- Solicitar al usuario que ingrese el n�mero de habitantes del municipio registrado 
en el paso anterior  y agregarlo a una lista llamada �habitantes�. 
(Repetir este paso para cada uno de los municipios registrados). 

3.- Crear dos nuevas variables que contengan la sumatoria y el promedio de los 
habitantes de los municipios ingresados, haciendo uso de las listas creadas en el paso 
anterior. 
4.- Mostrar el valor de estas dos nuevas variables al usuario usando print().
'''
# Declaraci�n de Variables
Municipios = []
Habitantes = []
TotalHabitantes = int(0)
Habitante = int(0)
PromedioHabitantes = float(0)
Bandera = False

for cont in range(3):
    Municipio = input('Captura el nombre del Municipio: ')
    Municipios.append(Municipio)
    # Se valida que el usuario Capture un numero entero
    Habitante = input('Captura La cantidad de habitantes del Municipio: ')
    
    try:
        Entero = int(Habitante)
        TotalHabitantes = TotalHabitantes + Entero
        Habitantes.append(Entero)
        Bandera = True       
    except ValueError:
        print("Lo que escribiste NO es un entero")
        Bandera = False 
        break
    
if Bandera:
    for cont in range(0, len(Municipios)):
        print(Municipios[cont])
        print(Habitantes[cont])

    print('El Total de Habitantes en los 3 Municipios es: '+ str (TotalHabitantes))
    PromedioHabitantes = TotalHabitantes/len(Habitantes)
    print('El Promedio de Habitantes en los 3 Municipios es: '+ str (PromedioHabitantes))

