class Vocation:
    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        return f"Nome personagem: {self.nome}."


class Mago(Vocation):
    def __init__(self, nome):
        super().__init__(nome)
        self.classe = "Mago"

    def exibir(self,):
        return f"Ficha \n Nome:{self.nome} \n Classe:{self.classe}"

    def fireboll(self):
        return f" Bola de fogo"


class Guerreiro(Vocation):
    def __init__(self, nome):
        super().__init__(nome)
        self.classe = "Guerreiro"

    def exibir(self):
        return f"Ficha \n Nome:{self.nome} \n Classe:{self.classe}"

    def corte(self):
        return f" Golpe cortante"


class BladeDancer(Mago, Guerreiro):
    # def __init__(self,nome):
    #     super().__init__(nome)
    #     self.classe="Blade Dancer"
    #
    # def dancer(self):
    #     return f" Dancer = {self.classe}"
    def vocacao(self):
        return f" Dancarino com espadas"


personagem1 = Vocation("Mark")
personagem2 = Mago("Richard")
personagem3 = Guerreiro("Fran")
personagem4 = BladeDancer("Anubiz")
print(personagem1.exibir())

print(personagem2.exibir())
print(personagem2.fireboll())

# print(personagem4.exibir())
print(personagem4.vocacao())
print(personagem4.fireboll())
print(personagem4.corte())
