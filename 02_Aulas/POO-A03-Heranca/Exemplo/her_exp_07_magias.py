class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        return f"Ficha do personagem\n Nome:{self.nome}"


class Mago(Personagem):
    def __init__(self, nome, dano):
        super().__init__(nome)
        self.dano = dano

    def BoladeFogo(self):
        return f"Acertou o alvo - {self.dano}"


class Guerreiro(Personagem):
    def __init__(self, nome, dano):
        super().__init__(nome)
        self.dano = dano

    def Espadada(self):
        return f"Acertou o alvo - {self.dano} de vida"


class BladeDancer(Mago, Guerreiro):
    def __init__(self, nome, dano):
        self.dano = dano
        self.nome = nome

    def BoladeFogo(self):
        return f"Acertou o alvo - {self.dano}"

    def Espadada(self):
        return f"Acertou o alvo - {self.dano}"


personagem1 = Guerreiro("Fabim", 5)
print(f"Ficha do personagem\n Nome:{personagem1.nome}")
print(f"Atacou com a Espada {personagem1.Espadada()}")

personagem2 = BladeDancer("FabinhoDançarino", 3)
print(f"Ficha do personagem\n Nome:{personagem2.nome}")
print(f"Atacou com a Espada {personagem2.Espadada()} dançando")
print(f"Atacou com sua habilidade magica {personagem2.BoladeFogo()} ")
