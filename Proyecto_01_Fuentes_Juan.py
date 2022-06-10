'''
Created on 19 may. 2022
@author: Juan Jaime Fuentes Uriarte
'''
# Variables Basicas para el programa

Usuarios = [
    ['jjfuentes', '123', 'admin'],
    ['jaime', '123', 'admin'],
    ['juan', '123', 'user'],
    ['pedro', '123', 'user']]
User = str("")
Pass = str("")
TipUser= str("")
Aux = bool(False)
# Ejecuci�n del Login
print("Bienvenido al Sistema de LifeStore")
Usuario = input("Usuario: ")
Contrasena = input("Contraseña:")

# #Inicia Ciclo para Validadción de usuario y realizar Procesos 
# Genara un ciclo con todos los usurios que se encuantran en la Variable Usuarios
# Si el usuario se encuentra en  la lista asigna los datos a sus respectivas Variables 
         
while (Aux == False):    
    #se obtienen los datos de la lista 
    for UserioInt in Usuarios:
        if ((Usuario in UserioInt) and (Contrasena in UserioInt)):
            User=  UserioInt[0]
            Pass=  UserioInt[1]
            TipUser= UserioInt[2]
        elif ((Usuario in UserioInt) and not(Contrasena in UserioInt)):
            User=  UserioInt[0]
            Pass=  UserioInt[1]
            TipUser= UserioInt[2]
        
    #Se valida  el usuario obtenido
    if ((Usuario.rstrip("") == User.rstrip("") and (Contrasena.rstrip("") != Pass.rstrip("")) and (Aux == False))):
        print("Intentar nuevamente")
        Contrasena = input("Contraseña:")
        #Aux = True #quitar solo pruebas
    elif ( (Usuario.rstrip(" ") != User.rstrip(" ")) and (Aux == False)):
        print("Añadir un nuevo usuario")
        Usuario = input("Usuario: ")
        Contrasena = input("Contraseña:")
        Usuarios.append([Usuario,Contrasena,"user"])       
        #Aux = True #quitar solo pruebas
    elif ((Usuario.rstrip(" ") == User.rstrip(" ")) and (Contrasena.rstrip("") == Pass.rstrip(""))):  # Valida que el Usuario tecledo por exista en la Lista                                            # Valida que la contraseña dada sea igual a la almacenada 
        print("Usuario Valido")
        Aux = True #quitar solo pruebas
        

