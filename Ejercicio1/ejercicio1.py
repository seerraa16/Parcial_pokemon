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
            raise ValueError("Health points must be between 1 and 100")
        if not 1 <= ataque <= 10:
            raise ValueError("Attack index must be between 1 and 10")
        if not 1 <= defensa <= 10:
            raise ValueError("Defense index must be between 1 and 10")            
    
