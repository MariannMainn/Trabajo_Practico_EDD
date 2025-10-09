#Estructura de Datos Arbol General
class NodoArbol :
    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol_Carpeta:
    def __init__(self):
        self.raiz = None
    
                # Metodos de Arbol

    def insertar_dato(self):
        pass
    def eliminar_dato(self):
        pass
    def buscar_dato(self):
        pass
    def recorrer_inorder(self):
        pass
    def recorrer_order(self):
        pass
    def recorrer_preorder(self):
        pass


                                    ####--CLASE CARPETA--####
class Carpeta:
    def __init__(self):
        self._carpeta_mensajes = Arbol_Carpeta()


                                #metodos de Carpeta
    #Crear carpeta 
    def crear_carpeta(self):
        pass

    # recibe un objeto mensaje/diccionario del servidor y lo Guarda en la carpeta
    def obtener_datos(self,dato):
        pass
    
    #mueve un mensaje de una carpeta/Nodo a otra
    def mover_dato(self,dato):
        pass
    
    #elimina un mensaje del arbol
    def eliminar_dato(self,dato):
        pass

    #listar mensajes
    def listar_dato(self):
        pass
    
    #permite leer un mensaje de la lista
    def leer_dato(self):
        pass