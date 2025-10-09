from mensaje import *
from carpeta import *

#clase usuario
class Persona:
    def __init__(self,nombre,apellido,edad):
        self._nombre= nombre
        self._apellido= apellido
        self._edad = edad


    def __str__(self):
        return f"nombre: {self._nombre}  apellido: {self._apellido}"

    #metodos
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

## Clase Contacto ###
    #PROXIMAMENTE


###                                 CLASE USUARIO                   ###

class Usuario(Persona):
    def __init__(self,correo,contrasenia,nombre,apellido,edad):
        super().__init__(nombre,apellido,edad)
        self.correo = correo
        self.contrasenia = contrasenia
        self.mensajes= Carpeta()
        self.contactos= Carpeta()


    ## Metodos de Clase ##

#  Metodo para editar los datos de usuario
    def editar_datos(self):
        pass

# Metodo para enviar mensajes a otro usuario
    def enviar_mensaje(self,texto,remitente,destinatario,asunto):
        mensaje = Mensaje(texto,remitente,destinatario,asunto)
        return mensaje

# este metodo muestra los mensajes guardados en la lista de mensajes
    def mostrar_mensajes(self):
        if len(self.mensajes) == 0:
            return "no hay mensajes"
        else:
            for mensaje in self.mensajes:
                return mensaje 

# contactos 
    def agregar_contacto(self):
        pass         # a implementar proximamente
    
    def mostrar_contactos(self):
        if len(self.contactos)== 0:
            return False
        else:
            for contacto in self.contactos:
                return contacto

