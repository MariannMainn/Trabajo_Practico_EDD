#Estructura de Datos Arbol General
class NodoArbol :
    def __init__(self,_remitente):
        self.dato = _remitente
        self.izquierda = None
        self.derecha = None

class Arbol_Carpeta:
    def __init__(self):
        self.raiz = None
    
                # Metodos de Arbol
    def instertar_recursivo(self,nodo,dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(dato)
            else:
                self.instertar_recursivo(nodo.izquierda,dato)
        
        elif dato > nodo.dato: # ->si remplazamos else, por esta linea , para que no se añadan datos duplicados
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(dato)
            else:
                self.instertar_recursivo(nodo.derecha,dato)
    def insertar_dato(self,dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self.instertar_recursivo(self.raiz,dato)
        

#Buscar elementos dentro del arbol
    def buscar_recursivo(self,nodo,dato):
            if nodo is None:
                return False
            if dato == nodo.dato:
                return True
            if dato < nodo.dato:
                return self.buscar_recursivo(nodo.izquierda,dato)
            else:
                return self.buscar_recursivo(nodo.derecha, dato)
    def buscar_dato(self,dato):
        return self.buscar_recursivo(self.raiz,dato)
    

#Metodo para recorrer la lista (InOrder: Izquierda-Centro-Derecha):
    def recorrido_inorder (self,nodo,resultado):
        if nodo:
            self.recorrido_inorder(nodo.izquierda,resultado)
            resultado.append(nodo.dato)
            self.recorrido_inorder(nodo.derecha,resultado)
    def inOrder(self):
        resultado = []
        self.recorrido_inorder(self.raiz,resultado)
        return resultado


#Metodo para recorrer la lista (PreOrder: Izquierda-Derecha-Centro):
    def recorrido_preOrder (self,nodo,resultado):
        if nodo:
            self.recorrido_preOrder(nodo.izquierda,resultado)
            self.recorrido_preOrder(nodo.derecha,resultado)
            resultado.append(nodo.dato)
    def preOrder(self):
        resultado = []
        self.recorrido_preOrder(self.raiz,resultado)
        return resultado


#Metodo para recorrer la lista (PostOrder: Centro-Izquierda-Derecha):
    def recorrido_postOrder (self,nodo,resultado):
        if nodo:
            resultado.append(nodo.dato)
            self.recorrido_postOrder(nodo.izquierda,resultado)
            self.recorrido_postOrder(nodo.derecho,resultado)
    def postOrder(self):
        resultado = []
        self.recorrido_postOrder(self.raiz,resultado)
        return resultado
    





                                    ####--CLASE CARPETA--####
class Carpeta:
    def __init__(self):
        self.mensajes = Arbol_Carpeta() # UNA CARPETA QUE ALMACENARA LOS MENSAJES NUEVOS 
        self.mensajes_nuevos = Arbol_Carpeta()  # UNA VEZ QUE LOS MENSAJES NUEVOS SON LEIDOS SON REMOVIDOS DE LA CARPETA MENSAJES Y ALMACENADOS EN ESTA CARPETA

                                #metodos de Carpeta

    # recibe un objeto mensaje/diccionario del servidor y lo Guarda en la carpeta/ARBOL MEDIANTE UNA LLAMADA AL METODO DEL ARBOL
    def insertar_mensajes(self,mensaje_obj):
        self.mensajes_nuevos.insertar_dato(mensaje_obj)


    #mueve un mensaje de una carpeta/NodoArbol a otra
    def mover_mensaje(self,mensaje_obj):
        pass 
    
    #elimina un mensaje del arbol
    def eliminar_mensaje(self,mensaje_obj):
        pass

    #RETORNA LOS MENSAJES ALMACENADOS DENTRO DEL ARBOL EN FORMATO LISTA
    def listar_mensajes(self):
        return self.mensajes_nuevos.inOrder()
    
    
    # RECIBE UN OBJETO DE TIPO MENSAJE Y LO ALMACENA EN EL ARBOL, ESTE METODO SE RELACIONA CON GUARDAR MENSAJE DE LA CLASE USUARIO.
    def obtener_mensaje(self,mensaje_obj):
        return self.mensajes.buscar_dato(mensaje_obj)
        


