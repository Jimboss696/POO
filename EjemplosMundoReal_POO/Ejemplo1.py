class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def hacer_reserva(self, evento):
        reserva = Reserva(self, evento)
        self.reservas.append(reserva)
        print(f"{self.nombre} ha hecho una reserva para {evento.nombre}.")

class Reserva:
    def __init__(self, usuario, evento):
        self.usuario = usuario
        self.evento = evento

class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha

# Creación de instancias y demostración de interacción
usuario1 = Usuario("Juan")
evento1 = Evento("Concierto", "01/01/2023")

usuario1.hacer_reserva(evento1)

# Se puede agregar más interacciones o situaciones según sea necesario