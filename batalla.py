
from random import randrange
from guerrero import Guerrero


class Batalla:
    def __init__(self, nombre, guerreroA, guerreroB, indiceDeAcierto, indiceDeGolpe, criterioDeAcierto):
        self.nombre = nombre
        self.guerreroA = guerreroA
        self.guerreroB = guerreroB
        self.indiceDeAcierto = indiceDeAcierto
        self.indiceDeGolpe = randrange(-10, 11, 1)
        self.criterioDeAcierto = criterioDeAcierto
        self.ronda = []

    def velocidadDeGuerrero(self, guerrero):
        print(self.guerrero.velocidad)
        return self.velocidad

    def asignacionOrdenDeTurno(self, ronda, guerreroA, guerreroB):
        # self.ronda = [self.guerreroA, self.guerreroB]
        self.ronda.append(self.guerreroA)
        self.ronda.append(self.guerreroB)
        print(self.ronda)
        self.ronda.sort(key=self.velocidadDeGuerrero)
        print(self.ronda)
        return self.ronda