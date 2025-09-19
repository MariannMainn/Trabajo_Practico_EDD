#clase mensaje
class Mensaje:
        def __init__(self,remitente, destinatario, asunto):
                self._mensaje= " "
                self._remitente= remitente
                self._destinatario= destinatario
                self._asunto= asunto

        #Metodos 
        def obtener_mensaje(self):
                return self._mensaje
        def redactarMensaje (self,nuevoMensaje):
                self._mensaje = nuevoMensaje

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
