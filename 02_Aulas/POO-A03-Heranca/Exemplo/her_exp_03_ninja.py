class Ninja:
    def __init__(self, nacao, vila):
        self.nacao = nacao
        self.vila = vila

    def ataca(self):
        print(f"Lança a Shuriken!")

    def defensa(self):
        print("Jutsu de substituição")


class Ambu(Ninja):
    def __init__(self, nacao, vila, vida):
        super().__init__(nacao, vila)
        self.vida = vida
        # self.nacao = nacao
        # self.vila = vila

    def vida_maior(self):
        if self.vida > 10:
            print("Vida cheia")
            return
        print("Vida baixa")

# n1 = Ninja("Fogo", "folha")
# print(f"{n1.nacao}, {n1.vila}")


# print(f"{n1.ataca()}")
# n1.defensa()
a1 = Ambu("Montanha", "Areia", 11)
print(f"{a1.nacao} e {a1.vila}, sua vida é {a1.vida}")
a1.defensa()
a1.ataca()
a1.vida_maior()
