#clase carpeta
class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre 
        self._mensajes = []
#metodos
    def guardarMensaje(self, texto):
        self._mensajes.append(texto)

    def agregarMensaje(self, texto):
        self.guardarMensaje(texto)

