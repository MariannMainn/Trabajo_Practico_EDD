from correo_servidor import servidorCorreo
#clase usuario
class usuario(servidorCorreo):
    def __init__(self, nombre, apellido, correo,contraseña):
        self._nombre= nombre
        self._apellido= apellido
        self._correo = correo
        self.__contraseña = contraseña

    def __str__(self):
        return f"nombre {self._usuario} apellido{self._apellido}"
    
    def enviar_mensaje(self):
        return super().enviar_mensaje()
    def obtener_Mensajes(self):
        return super().obtener_Mensajes()
    


