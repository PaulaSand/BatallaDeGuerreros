"""Programe un simulador de batallas entre dos guerreros siguiendo el siguiente diagrama de clases y las reglas
Guerrero:
nombre string
vida int
fuerza int
presiciòn float
velocidad float
defensa float
----------------
golpear(Guerrero): void

Consideremos que están luchando guerreroA contra guerreroB:
-Se golpea por turnos
-Comienza el jugador con mayor velocidad
-Si guerreroA intenta golpear a guerreroB, la probabilidad de acierto es:
(guerreroA.precision - guerreroB.velocidad) / 100
-Si guerreroA golpea guerreroB, el daño será:
max(guerreroA.fuerza - guerreroB.defensa + randrange(-10, 11), 1)
-La pelea finaliza cuando algún guerrero llega a vida 0

Para realizar el simulador de batallas, se sugiere que se realice una clase auxiliar que
se denomine “Pelea” o “Simulador de batalla” y que de alguna manera inicialice por parametro del constructor
a los guerreros, y con un método iniciar batalla, haga pelear a los guerreros y nos devuelva el ganador de la batalla.
ADICIONAL: se podría guardar o realizar un “logueo” o guardado de todos los turnos que pasaron en la batalla.
También se podría realizar que, en vez de devolver el ganador de la batalla, nos devuelva un objeto que contenga datos
relevantes de la batalla y que ese mismo objeto posea un método que sea devolver ganador, de esa forma tendriamos la
solución del problema más desacoplada."""


from batalla import Batalla
from guerrero import Guerrero

print("hola")

guerreroA = Guerrero("JuanElElfo",40,70,50,60)
guerreroB = Guerrero("OscarELEnano",80,35,40,70)
batalla1 = Batalla("batalla1",guerreroA, guerreroB, 100 ,[1000,2000,3000,4000], 1)

print(guerreroA)
print(guerreroB)

batalla1.asignacionOrdenDeTurno(batalla1.ronda, guerreroA, guerreroB)
