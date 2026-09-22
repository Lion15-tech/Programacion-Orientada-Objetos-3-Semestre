class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Cada canal debe enviar de forma distinta")

class NotificacionEmail(Notificacion):
    def __init__(self, mensaje, correo_destino):
        super().__init__(mensaje)
        self.correo_destino = correo_destino

    def enviar(self):
        print(f"Enviando Email a {self.correo_destino}: {self.mensaje}")

class NotificacionSMS(Notificacion):
    def __init__(self, mensaje, numero_destino):
        super().__init__(mensaje)
        self.numero_destino = numero_destino

    def enviar(self):
        print(f"Enviando SMS a {self.numero_destino}: {self.mensaje}")


# Código de prueba para validar tu solución:
email = NotificacionEmail("Tu código de verificación es 1234", "usuario@gmail.com")
sms = NotificacionSMS("Tu paquete ha llegado", "5512345678")

email.enviar()
# Debería imprimir: Enviando Email a usuario@gmail.com: Tu código de verificación es 1234

sms.enviar()
# Debería imprimir: Enviando SMS a 5512345678: Tu paquete ha llegado