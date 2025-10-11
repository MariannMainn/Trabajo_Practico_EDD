from usuario import *
from carpeta import *
from arbol_estructure import *


# Interfaz del Servidor
from abc import ABC,abstractmethod
class Servidor(ABC):
    def __init__(self):
        pass

        #METODOS ABSTRACTOS DE CLASE
    @abstractmethod
    def enviar_mensaje(self):
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
        self.list_user= Arbol_Carpeta_users()


            #Metodos de clase

    #CREA UN OBJETO DE TIPO USUARIO, CON LOS ARGUMENTOS REQUERIDOS Y LUEGO LO ALMACENA EN UNA LISTA(PROVISIONAL) PARA SU POSTERIOR USO.
    def crear_usuario(self,nombre,apellido,edad,correo,contrasenia):
        nuevo_Usuario = Usuario(correo,contrasenia,nombre,apellido,edad)
        self.list_user.insertar_dato(nuevo_Usuario) 

    #ELIMINA UN ELEMENTO/USUARIO DE LA LISTA 
    def eliminar_usuario(self):
        pass

    def buscar_usuario(self,dato):
        return self.list_user.buscar_dato(dato)

    
    #MUESTRA TODOS LOS ELEMENTOS ALMACENADOS EN LA LISTA CON UN CICLO FOR
    def mostrar_usuario(self):
        dato =self.list_user.inOrder()
        for datos in dato:
            print(datos)
    
        

    #ENVIA UN OBJETO DE TIPO MENSAJE A LA CARPETA MENSAJES DEL USUARIO
    def enviar_mensaje(self,mensaje,destinatario):
            usuario = self.buscar_usuario(destinatario)
            usuario.guardar_mensajes(mensaje)


    #METODO PARA VERIFICAR/VALIDAR CONTRASEÑAS Y USUARIOS
    def sesion(self,correo,contrasenia):
        pass





#PRUEBAS DE CODIGO...
if __name__ == "__main__":
    correo = Correo()
    #CREA DOS USUARIOS Y LOS GUARDA EN LA LISTA DE LA CLASE CORREO
    correo.crear_usuario("alexa","sanchez",24,"alexa@correoRandom.com","12345")
    correo.crear_usuario("rick","martinez",32,"RickMart@correoRandom.com","abc")
    correo.crear_usuario("peter","gomez",12,"PitGomes@correoRandom.com","12345")
    correo.crear_usuario("Daniel","alonso",32,"daniels@correoRandom.com","abc")

    correo.mostrar_usuario()

    print()
    print("Busqueda de un usuario en la lista")
    usuario =correo.buscar_usuario("RickMart@correoRandom.com")
    print(usuario)
    mensaje =usuario.crear_mensaje("hola me presento",usuario.correo,"daniels@correoRandom.com","saludo...")
    correo.enviar_mensaje(mensaje,"daniels@correoRandom.com")
    print()
    print("otro usuario")
    usuario2 =correo.buscar_usuario("daniels@correoRandom.com")
    print(usuario2)
    print("mensajes recibidos...")
    print()
    print(usuario2.mostrar_mensajes())




    