class Caneca:
    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = False

    def encher(self):
        if self.status == True:
            print(f"A caneca {self.nome} já está cheia.")
        else:
            print(f"Enchendo...")
            self.status = True

    def beber(self):
        if self.status == True:
            print(f"bebendo")
            self.status = False
            return
        print(f"A caneca {self.nome} esta vazia!")


class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__("Caneca Londrina", "Cidade de Londres", "Branca")
        # self.nome = "Caneca Londrina"
        # self.logo = "Cidade de Londres"
        # self.cor = "Branca"
        self.status = False


c1 = CanecaLondrina()
c1.beber()
c1.encher()
c1.encher()
c1.beber()
c1.encher()
print(f"{c1.nome}")
