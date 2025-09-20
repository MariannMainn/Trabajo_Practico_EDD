#clase usuario
class Usuario():
    def __init__(self, nombre, apellido, correo, edad, contrasenia):
        self._nombre= nombre
        self._apellido= apellido
        self._correo = correo
        self._edad = edad
        self.__contrasenia = contrasenia

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

    def obtener_contrasenia(self):
        return self.__contrasenia
    def cambiar_contrasenia(self,nuevaContra):
        self.__contrasenia = nuevaContra


