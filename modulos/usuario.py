from mensaje import *
from carpeta import *


#clase PERSONA.
class Persona:
    def __init__(self,nombre,apellido,edad):
        self._nombre= nombre
        self._apellido= apellido
        self._edad = edad

    def __str__(self):
        return f"nombre: {self._nombre}  apellido: {self._apellido}"
    
                                   ##METODOS DE CLASE  ##
    #INTENTO DE GETTERS Y SETTERS
    def obtener_nombre(self):
        return self._nombre
    def cambiar_nombre(self,nuevoNombre):
        self._nombre = nuevoNombre

    def obtener_apellido(self):
        return self._apellido
    def cambiar_apellido(self,nuevoApellido):
        self._apellido = nuevoApellido

    def obtener_edad(self):
        return self._edad
    def cambiar_edad(self,NuevaEdad):
        self._edad = NuevaEdad

            ###                                 CLASE USUARIO                   ###

#CLASE USUARIO QUE HEREDA ATRIBUTOS DE LA CLASE PERSONA.
class Usuario(Persona):

    def __init__(self,correo,contrasenia,nombre,apellido,edad):
        super().__init__(nombre,apellido,edad)
        self.correo = correo    #ATRIBUTOS DE CLASE
        self.contrasenia = contrasenia  #ATRIBUTOS DE CLASE
        self.mensajes= Carpeta() #ARBOL CON SUS METODOS Y ATRIBUTOS 


    def __str__(self):
        return f"nombre: {self._nombre}  apellido: {self._apellido}. Correo {self.correo}"


                                ## Metodos de Clase ##  
    #Metodo de comparacion dunder 
    def __lt__(self,dato):
                return self.correo < dato.correo
    def __eq__(self,dato):
                return self.correo == dato.correo
    def __gt__(self,dato):
                return self.correo > dato.correo
    


#  Metodo para editar los datos de usuario
    def editar_datos(self):
        pass

# Metodo para enviar mensajes a otro usuario / CREA UN OBJETO DE TIPO MENSAJE Y LO RETORNA PARA SU POSTERIOR ENVIO
    def crear_mensaje(self,texto,remitente,destinatario,asunto):
        # Crea un objeto de tipo mensaje y lo devuelve.
        mensaje = Mensaje(texto,remitente,destinatario,asunto)
        return mensaje



# este metodo muestra los mensajes guardados en la lista de mensajes/ REALIZA UN LLAMADO A UN METODO DE LA CLASE CARPETA/ARBOL
    def mostrar_mensajes(self):
        lista_mensajes =  self.mensajes.listar_mensajes()
        for mensajes in lista_mensajes:
             return mensajes
        
#METODO QUE ALMACENA UN MENSAJE EN LA CARPETA/ARBOL ESTE METODO REALIZA UN LLAMADO A UN METODO DE LA CLASE ARBOL/CARPETA Y LE PASA COMO ARGUMENTO EL MENSAJE
    #GUARDA RELACION CON UN METODO DE LA CLASE CARPETA
    def guardar_mensajes(self,mensaje):
        self.mensajes.insertar_mensajes(mensaje)



