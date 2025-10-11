#clase mensaje
class Mensaje:
        def __init__(self, texto, remitente, destinatario, asunto):
                self._texto= texto
                self._remitente= remitente
                self._destinatario= destinatario
                self._asunto= asunto

        #metodo Dunder de comparacion
        def __lt__(self,dato):
                return self._remitente < dato._remitente
        def __eq__(self,dato):
                return self._remitente == dato._remitente
        def __gt__(self,dato):
                return self._remitente > dato._remitente
        
        
        #DEVUELVE UN STRING O CADENA CON LOS DATOS DEL MENSAJE
        def __str__ (self):
                asunto = "\nAsunto: "
                remitente= "\tDe: "
                texto = "\nmensaje: \n"
                mensaje = "\t"
                mensaje_format = asunto + self._asunto + remitente + self._remitente + texto + mensaje+mensaje +  self._texto
                return  mensaje_format
        
        # INTENTO DE SETTERS Y GETTERS
        def obtener_texto(self):
                return self._texto
        def redactarTexto (self,nuevoMensaje):
                self._texto = nuevoMensaje

        def obtener_remitente(self):
                return self._remitente
        def cambiar_remitente (self,nuevoRem):
                self._remitente = nuevoRem

        def obtener_destinatario(self):
                return self._destinatario
        def cambiarDestinatario (self,nuevodestinatario):
                self._destinatario = nuevodestinatario

        def obtener_asunto(self):
                return self._asunto
        def cambiarAsunto (self,nuevoAsunto):
                self._asunto = nuevoAsunto

        #METODOS?...