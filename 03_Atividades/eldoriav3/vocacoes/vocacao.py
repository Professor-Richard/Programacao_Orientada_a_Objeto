class VocacaoBase:
    """Classe base para todas as vocações"""

    def __init__(self, nome: str, modificadores: dict):
        self.nome = nome
        self.modificadores = modificadores

    def aplicar_modificadores(self, jogador):
        """Aplica os modificadores da vocação ao jogador"""
        jogador.poder += self.modificadores.get("poder", 0)
        jogador.defesa += self.modificadores.get("defesa", 0)
        jogador.vida_maxima += self.modificadores.get("vida_maxima", 0)
        jogador.esquiva += self.modificadores.get("esquiva", 0)
        jogador.vida_atual = jogador.vida_maxima

        print(f"Vocacao {self.nome} aplicada!")

    def __str__(self):
        return self.nome


class Guerreiro(VocacaoBase):
    def __init__(self):
        super().__init__(
            nome="Guerreiro",
            modificadores={
                "poder": 2,
                "defesa": 1,
                "vida_maxima": 0,
                "esquiva": 0
            }
        )


class Arqueiro(VocacaoBase):
    def __init__(self):
        super().__init__(
            nome="Arqueiro",
            modificadores={
                "poder": 1,
                "defesa": 0,
                "vida_maxima": 0,
                "esquiva": 2
            }
        )


class Paladino(VocacaoBase):
    def __init__(self):
        super().__init__(
            nome="Paladino",
            modificadores={
                "poder": 1,
                "defesa": 2,
                "vida_maxima": 1,
                "esquiva": 0
            }
        )


class Ladino(VocacaoBase):
    def __init__(self):
        super().__init__(
            nome="Ladino",
            modificadores={
                "poder": 1,
                "defesa": -1,
                "vida_maxima": 0,
                "esquiva": 2
            }
        )


class Mago(VocacaoBase):
    def __init__(self):
        super().__init__(
            nome="Mago",
            modificadores={
                "poder": 3,
                "defesa": -2,
                "vida_maxima": -1,
                "esquiva": 1
            }
        )


class Barbaro(VocacaoBase):
    def __init__(self):
        super().__init__(
            nome="Bárbaro",
            modificadores={
                "poder": 3,
                "defesa": 0,
                "vida_maxima": 2,
                "esquiva": -2
            }
        )


class Clerigo(VocacaoBase):
    def __init__(self):
        super().__init__(
            nome="Clérigo",
            modificadores={
                "poder": 0,
                "defesa": 2,
                "vida_maxima": 2,
                "esquiva": 0
            }
        )


# Dicionário para acessar todas as vocações facilmente
VOCACOES = {
    "guerreiro": Guerreiro,
    "arqueiro": Arqueiro,
    "paladino": Paladino,
    "ladino": Ladino,
    "mago": Mago,
    "barbaro": Barbaro,
    "clerigo": Clerigo
}


def criar_vocacao(nome: str):
    """Factory function para criar uma vocação pelo nome"""
    nome = nome.lower().strip()
    if nome in VOCACOES:
        return VOCACOES[nome]()
    else:
        print(
            f"Vocação '{nome}' não encontrada. Usando Guerreiro como padrão.")
        return Guerreiro()


def listar_vocacoes():
    """Retorna uma lista com todas as vocações disponíveis"""
    return list(VOCACOES.keys())


if __name__ == "__main__":
    from entities.jogador import Jogador

    print("=== TESTE DAS VOCAÇÕES ===\n")

    # Listar todas as vocações
    print("Vocações disponíveis:")
    for nome in listar_vocacoes():
        print(f"  - {nome.capitalize()}")

    print("\n" + "="*40)

    # Testar cada vocação
    for nome_vocacao in listar_vocacoes():
        print(f"\n--- Testando {nome_vocacao.capitalize()} ---")

        # Cria jogador base
        jogador = Jogador(f"Heroi_{nome_vocacao}")
        print(f"Antes: Poder={jogador.poder}, Defesa={jogador.defesa}, "
              f"Vida={jogador.vida_maxima}, Esquiva={jogador.esquiva}")

        # Aplica vocação
        vocacao = criar_vocacao(nome_vocacao)
        vocacao.aplicar_modificadores(jogador)

        print(f"Depois: Poder={jogador.poder}, Defesa={jogador.defesa}, "
              f"Vida={jogador.vida_maxima}, Esquiva={jogador.esquiva}")
        print(f"Modificadores: {vocacao.modificadores}")
