# Herança Simples
class Veiculo:
    def tipo(self):
        return "Veículo"


class Carro(Veiculo):
    def rodas(self):
        return 4


class Esportivo(Carro):
    def velocidade_maxima(self):
        return 300


# Herança Múltipla
# Uma classe pode herdar de múltiplas classes.

class Mamifero:
    def caracteristica(self):
        return "Amamenta os filhotes"


class Ave:
    def caracteristica(self):
        return "Tem penas"


class Morcego(Mamifero, Ave):
    pass


morcego = Morcego()
print(morcego.caracteristica())  # Amamenta os filhotes
