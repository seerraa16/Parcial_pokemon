class pokemon:
    def __init__(self, Id, nombre, tipoArma, salud, ataque, defensa):
        self.Id = Id
        self.nombre = nombre
        self.tipoArma = tipoArma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
    def salud():
        salud = 1 <= salud <= 100
        return salud
    def ataque():
        ataque = 1 <= ataque <= 10
        return ataque
    def defensa(): 
        defensa = 1 <= defensa <= 10
        return defensa
    def tipoArma():
        tipoArma = ["Puñetazo", "Patada", "Codazo", "Cabezazo"]
        return tipoArma 
