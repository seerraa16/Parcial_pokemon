class pokemon:
    def __init__(self, Id, nombre, tipoArma, salud, ataque, defensa):
        self.Id = Id
        self.nombre = nombre
        self.tipoArma = tipoArma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
    def salud():
        salud = int(input("Ingrese la salud del pokemon: "))
        if 1 <= salud <= 100:
            return salud
        else:
            print("Ingrese un valor entre 1 y 100")
    def ataque():
        ataque = int(input("Ingrese el ataque del pokemon: "))
        if 1 <= ataque <= 10:
            return ataque
    def defensa(): 
        defensa = int(input("Ingrese la defensa del pokemon: "))
        if 1 <= defensa <= 10:
            return defensa
    def tipoArma():
        tipoArma = ["Puñetazo", "Patada", "Codazo", "Cabezazo"]
        return tipoArma 
