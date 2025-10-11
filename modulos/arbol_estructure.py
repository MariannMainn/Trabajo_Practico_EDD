#Estructura de Datos Arbol General
class NodoUser :
    def __init__(self,valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol_Carpeta_users:
    def __init__(self):
        self.raiz = None
    
                # Metodos de Arbol

    def insertar_dato(self,objeto):
        if self.raiz is None:
            self.raiz = NodoUser(objeto)
        else:
            self.instertar_recursivo(self.raiz,objeto)

            ####################################################
    def instertar_recursivo(self,nodo_actual,objeto):
        if objeto < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoUser(objeto)
            else:
                self.instertar_recursivo(nodo_actual.izquierda,objeto)
        
        elif objeto > nodo_actual.valor: # ->si remplazamos else, por esta linea , para que no se añadan datos duplicados
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoUser(objeto)
            else:
                self.instertar_recursivo(nodo_actual.derecha,objeto)
        

#Buscar elementos dentro del arbol
    def buscar_dato(self,dato):
        return self.buscar_recursivo(self.raiz,dato)
                                ##############################
    def buscar_recursivo(self,nodo,dato):
            if nodo is None or nodo.valor.correo == dato:
                return nodo.valor if nodo else None
            
            if dato == nodo.valor.correo:
                return nodo.valor
            
            if dato < nodo.valor.correo:
                return self.buscar_recursivo(nodo.izquierda,dato)
            
            else:
                return self.buscar_recursivo(nodo.derecha, dato)
    

#Metodo para recorrer la lista (InOrder: Izquierda-Centro-Derecha):
    def recorrido_inorder (self,nodo,resultado):
        if nodo:
            self.recorrido_inorder(nodo.izquierda,resultado)
            resultado.append(nodo.valor)
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
    



