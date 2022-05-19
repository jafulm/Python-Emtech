'''
Creado on 12 may. 2022
@author: Juan Jaime Fuentes Uriarte
'''
#Apartado de Declaración de Variables y sus tipos e Inicialización
TextoCabecera = """Información de La Secretaría de Economía
        del estado de Sinaloa        
"""
SuperficiEstado = int (57365)
PresipitacionAnual = float (790.1) 
PoblacionHombres = int (1494815)
PoblacionMujeres = int (1532128)
PoblacionTotal = PoblacionHombres + PoblacionMujeres
PorCul = float (33.15)
PorMaz = float (16.57)
TempMedAnual = float (25.45)
PorTotal2Ciudades = PorCul+PorMaz
Clima = ["cálido", "subhúmedo", "seco", "semiseco"]
# Desplegado de Información Comando Print
print(TextoCabecera)
print("La superficie del Estado es "+ str (SuperficiEstado))
print("La Presipitación anual del Estado es "+ str (PresipitacionAnual))
print("La Población de Hombres en Sinaloa es: " + str (PoblacionHombres))
print("La Población de Mujeres en Sinaloa es: " + str (PoblacionTotal))
print("La Población Total en Sinaloa es: " + str (PoblacionTotal))
print("El porcentaje de la población de la ciudad de Culiacán es :" + str(PorCul))
print("El porcentaje de la población de la ciudad de Mazatlán es :" + str(PorMaz))
print("El porcentaje de la población de las dos ciudades es :" + str(PorTotal2Ciudades)+"%")
print("La temperatura media del estado es :" + str(TempMedAnual)+"°")
print("Tipos de Clima del Estado")
for TiposClima in Clima:
    print(TiposClima)