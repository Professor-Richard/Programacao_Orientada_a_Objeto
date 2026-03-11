class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        pass

    def beber(self):
        pass


class Gato(Animal):
    # pass
    def __init__(self, nome, cor, id=1):
        super().__init__(nome, cor)
        self.id = id
        self.tipo = "Gato"


class Cao(Animal):
    # pass
    def __init__(self, nome, cor, id=2):
        super().__init__(nome, cor)
        self.id = id
        self.tipo = "Cao"

    # self.nome = nome
    # self.tipo = tipo
    # self.cor = cor


gato = Animal("bolinha", "Branca")
cachorro = Animal("Rex", "Preto")
print(f"{gato.nome}, {gato.cor}")
print(f"{cachorro.nome},{cachorro.cor}")
g1 = Gato("nome_gato", "cor_gato")
c1 = Cao("cao_nome", "cao_cor")
print(f"{g1.nome}, {g1.cor}, {g1.tipo} ")
print(f"{c1.nome}, {c1.cor}, {c1.tipo} ")
