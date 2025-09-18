#clase carpeta
from correo_servidor import servidorCorreo

class carpeta(servidorCorreo):
        def __init__(self):
            self._mensajes = []


        def obtener_Mensajes(self):
            return super().obtener_Mensajes()
        
        def enviar_mensaje(self):
            return super().enviar_mensaje()
        
        def listar_mensajes(self,mensaje):
            pass


