#clase usuario
class usuario:
    def __init__(self, usuario, correo):
        self.usuario= usuario 
        self.correo= correo
        
#clase mensaje
class mensaje:
    def __init__(self, mensaje, remitente, destinatario, asunto):
                self.mensaje= mensaje
                self.remitente= remitente
                self.destinatario= destinatario
                self.asunto= asunto
                
                
    def __str__(self):
            return f"{self.asunto} (de: {self.remitente})"
                
#clase carpeta
class carpeta:
    def __init__(self, usuario):
            self.usuario= usuario
            self.mensajes= ()
                        
                        
    def agregar_mensajes(self, mensaje):
                self.mensajes.append(mensaje)
                                            
    def obtener_mensajes(self):
                return self.mensajes
        
#clase ServidorCorreo                           
class servidorCorreo:
    def __init__(self):
        #sirve para guardar usuarios en las carpetas
        self.usuarios= ()
        self.carpetas= ()
        
    def registar_usuario(self, usuario):
            #agrega un usuario al servidor y crea sus carpetas
            self.usuario(usuario.correo)== usuario
            self.carpetas(usuario.correo)== {
            "Inbox":("Inbox"),
            "Enviados": ("Enviados")
                }
            
    def enviar_mensaje(self, mensaje):
            #guarda el mensaje en enviados del remitente y en inbox del destinatario
            
            #carpeta del remitente
            self.carpetas(mensaje.remitente)("enviados"). agregar_mensaje(mensaje)
            
            #carpeta del destinatario
            
            if mensaje.destinatario in self.usuario:
                self.carpetas(mensaje.destinatario)("inbox"). agregar_mensaje(mensaje)
                
            else:
                print("el destinatario no se encuentra en el servidor")
                
                
            
                            
                            
                            
        
        

        
