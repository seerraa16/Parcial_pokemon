import random 
class pokemon:
    def __init__(self, Id, nombre, tipoArma, salud, ataque, defensa):
        self.Id = Id
        self.nombre = nombre
        self.tipoArma = tipoArma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

        
        if not 1 <= salud <= 100:
            print("El valor de la salud deve ser entre 1 y 100")
        if not 1 <= ataque <= 10:
            print("El ataque debe estar entre 1 y 10")
        if not 1 <= defensa <= 10:
            print("La defensa debe estar entre 1 y 10")
        if not Id == int:
            print("El Id debe ser un numero entero")
    
