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
    def crear_usuario(self,nombre,apellido,edad,correo,contrasenia):
        nuevo_Usuario = Usuario(correo,contrasenia,nombre,apellido,edad)
        self.usuarios.append(nuevo_Usuario)

    
    def eliminar_usuario(self):
        return super().eliminar_usuario()
    
    def mostrar_usuario(self):
        if len(self.usuarios)== 0 :
            return False
        else:
            for usuario in self.usuarios:
                print(usuario.correo)
                print("//")
        

    def destinar_mensaje(self,mensaje,destinatario):
        for usuario in self.usuarios:
            if destinatario == usuario.correo:
                usuario.mensajes.append(mensaje)


    
    
    def sesion(self,correo,contrasenia):
        if len(self.usuarios)== 0 :
            return False
        for usuario in self.usuarios:
            if (correo == usuario.correo) and (contrasenia == usuario.contrasenia):
                    return usuario


if __name__ == "__main__":
    correo = Correo()
    correo.crear_usuario("alexa","sanchez",24,"alexa@correoRandom.com","12345")
    correo.crear_usuario("rick","martinez",32,"RickMart@correoRandom.com","abc")
    correo.mostrar_usuario()
    print()
    user=correo.sesion("alexa@correoRandom.com","12345")
    print(user)
    print("enviando mensaje")
    correo.destinar_mensaje(user.enviar_mensaje("hola mi nombre es alexa y queria dejarte un mensaje",user.correo,"RickMart@correoRandom.com","saludo"),"RickMart@correoRandom.com")
    print()
    print("otro usuario recibiendo el mensaje")
    user2=correo.sesion("RickMart@correoRandom.com","abc")
    print(user2)
    print(user2.mostrar_mensajes())

