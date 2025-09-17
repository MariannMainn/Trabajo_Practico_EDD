#clase usuario
class usuario:
    def __init__(self, nombre, apellido, correo,contraseña):
        self._nombre= nombre
        self._apellido= apellido
        self._correo = correo
        self.__contraseña = contraseña

    def __str__(self):
        return f"nombre {self._usuario} apellifo{self._apellido}"


