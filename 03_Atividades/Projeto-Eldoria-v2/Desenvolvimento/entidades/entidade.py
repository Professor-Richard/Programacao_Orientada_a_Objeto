class Entidade:
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, esquiva: int):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.esquiva = esquiva

    def esta_vivo(self) -> bool:
        return self.vida_atual > 0

    def receber_dano(self, dano: int):
        self.vida_atual -= dano
        if self.vida_atual < 0:
            self.vida_atual = 0

    def curar(self, valor: int):
        self.vida_atual += valor
        if self.vida_atual > self.vida_maxima:
            self.vida_atual = self.vida_maxima


guerreiro = Entidade("Guerreiro", 5, 3, 10, 3)
print(guerreiro.nome)
print(guerreiro.vida_atual)
print(guerreiro.esta_vivo())

guerreiro.receber_dano(8)
print(guerreiro.vida_atual)
print(guerreiro.esta_vivo())

guerreiro.curar(20)
print(guerreiro.vida_atual)


guerreiro.receber_dano(15)
print(guerreiro.vida_atual)
print(guerreiro.esta_vivo())
