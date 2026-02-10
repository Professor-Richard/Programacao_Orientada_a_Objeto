class Cpf:
    def __init__ (self,nome,idade):
        self.nome=nome
        self.idade=idade

    def status(self):
        return print(f"Seu nome eh {self.nome} e sua idade eh: {self.idade}")


professor1=Cpf("Richard",35)

# print(professor1.status())
professor1.status()