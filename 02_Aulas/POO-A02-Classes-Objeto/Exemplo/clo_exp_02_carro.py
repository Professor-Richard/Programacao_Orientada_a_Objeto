class Carro:

    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        return f"{self.modelo} está ligado!"


# criando um objeto (instância)
meu_carro = Carro("vermelho", "Fusca", 1980)

# chamando o método
print(meu_carro.ligar())
