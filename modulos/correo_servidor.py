from usuario import *


# Interfaz del Servidor
from abc import ABC,abstractmethod
class Servidor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def destinar_mensaje(self):
        pass

    @abstractmethod
    def crear_usuario(self):
        pass

    @abstractmethod
    def mostrar_usuario(self):
        pass

    @abstractmethod
    def eliminar_usuario(self):
        pass


############           CLASE SERVIDOR CORREO                ###############
class Correo (Servidor):
    def __init__(self):
        super().__init__()
        self.usuarios = []


            #Metodos de clase

    #crear un nuevo Usuario y añadirlo a la lista de usuarios
    def crear_usuario(self,nombre,apellido,edad,correo,contrasenia):
        self.usuarios.append(nuevo_Usuario = Usuario(correo,contrasenia,nombre,apellido,edad))

    #Elimina un usuario especifico de la lista
    def eliminar_usuario(self):
        return super().eliminar_usuario()
    
    # Muestra una lista con todos los usuarios dentro de la lista /cambiar o eliminar metodo segun convenga
    def mostrar_usuario(self):
        if len(self.usuarios)== 0 :
            return False
        else:
            for usuario in self.usuarios:
                print(usuario.correo)
                print("//")
        

    #Permite el envio de mensajes a otros usuarios 
    def destinar_mensaje(self,mensaje,destinatario):
        for usuario in self.usuarios:
            if destinatario == usuario.correo:
                usuario.mensajes.append(mensaje)

    # Validacion de credenciales para acceder a los datos de usuario/como iniciar sesion o modificarlos
    def validar_datos(self,correo,contrasenia):
            pass

    # Retorna los datos de usuario si el metodo VALIDAR es TRUE
    def sesion(self,correo,contrasenia):
            pass