class Guerrero:
    def __init__(self, nombre, fuerza, precision, velocidad, defensa):
        self.nombre = nombre
        self.vida = 100
        self.fuerza = fuerza
        self.precision = precision
        self.velocidad = velocidad
        self.defensa = defensa

    def __str__(self):
        return ("Nombre: " + self.nombre + ", Fuerza:" + str(self.fuerza) + ", Presicion:" + str(
            self.precision) + ", Velocidad:" + str(self.velocidad) + ", Defensa:" + str(
            self.defensa) + ", Vida: " + str(self.vida))
