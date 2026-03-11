from entidade import Entidade


class Jogador(Entidade):
    def __init__(self, nome, poder, defesa, vida_maxima, esquiva, raca, vocacao):
        super().__init__(nome, poder, defesa, vida_maxima, esquiva)

        self.nivel = 1
        self.experiencia = 0
        self.inventario = []
        self.raca = raca
        self.vocacao = vocacao
