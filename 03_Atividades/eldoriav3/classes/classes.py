class RacaBase:
    """Classe base para todas as raças"""

    def __init__(self, nome: str, modificadores: dict):
        self.nome = nome
        self.modificadores = modificadores

    def aplicar_modificadores(self, jogador):
        """Aplica os modificadores da raça ao jogador"""
        jogador.poder += self.modificadores.get("poder", 0)
        jogador.defesa += self.modificadores.get("defesa", 0)
        jogador.vida_maxima += self.modificadores.get("vida_maxima", 0)
        jogador.esquiva += self.modificadores.get("esquiva", 0)
        jogador.vida_atual = jogador.vida_maxima

        print(f"Raça {self.nome} aplicada!")

    def __str__(self):
        return self.nome


class Humano(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Humano",
            modificadores={
                "poder": 1,
                "defesa": 1,
                "vida_maxima": 1,
                "esquiva": 1
            }
        )


class Elfo(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Elfo",
            modificadores={
                "poder": 1,
                "defesa": -1,
                "vida_maxima": 0,
                "esquiva": 2
            }
        )


class Anao(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Anão",
            modificadores={
                "poder": 1,
                "defesa": 1,
                "vida_maxima": 2,
                "esquiva": -1
            }
        )


class Halfling(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Halfling",
            modificadores={
                "poder": 0,
                "defesa": 0,
                "vida_maxima": -1,
                "esquiva": 3
            }
        )


class Draconato(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Draconato",
            modificadores={
                "poder": 2,
                "defesa": 2,
                "vida_maxima": 1,
                "esquiva": -2
            }
        )


class MeioElfo(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Meio-Elfo",
            modificadores={
                "poder": 1,
                "defesa": 0,
                "vida_maxima": 0,
                "esquiva": 1
            }
        )


class MeioOrc(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Meio-Orc",
            modificadores={
                "poder": 3,
                "defesa": 1,
                "vida_maxima": 2,
                "esquiva": -3
            }
        )


class Gnomo(RacaBase):
    def __init__(self):
        super().__init__(
            nome="Gnomo",
            modificadores={
                "poder": 0,
                "defesa": 1,
                "vida_maxima": -1,
                "esquiva": 2
            }
        )


# Dicionário para acessar todas as raças facilmente
RACAS = {
    "humano": Humano,
    "elfo": Elfo,
    "anao": Anao,
    "halfling": Halfling,
    "draconato": Draconato,
    "meio-elfo": MeioElfo,
    "meio-orc": MeioOrc,
    "gnomo": Gnomo
}


def criar_raca(nome: str):
    """Factory function para criar uma raça pelo nome"""
    nome = nome.lower().strip()
    if nome in RACAS:
        return RACAS[nome]()
    else:
        print(f"Raça '{nome}' não encontrada. Usando Humano como padrão.")
        return Humano()


def listar_racas():
    """Retorna uma lista com todas as raças disponíveis"""
    return list(RACAS.keys())


if __name__ == "__main__":
    from entities.jogador import Jogador

    print("=== TESTE DAS RAÇAS ===\n")

    # Listar todas as raças
    print("Raças disponíveis:")
    for nome in listar_racas():
        print(f"  - {nome.capitalize()}")

    print("\n" + "="*40)

    # Testar cada raça
    for nome_raca in listar_racas():
        print(f"\n--- Testando {nome_raca.capitalize()} ---")

        # Cria jogador base
        jogador = Jogador(f"Heroi_{nome_raca}")
        print(f"Antes: Poder={jogador.poder}, Defesa={jogador.defesa}, "
              f"Vida={jogador.vida_maxima}, Esquiva={jogador.esquiva}")

        # Aplica raça
        raca = criar_raca(nome_raca)
        raca.aplicar_modificadores(jogador)

        print(f"Depois: Poder={jogador.poder}, Defesa={jogador.defesa}, "
              f"Vida={jogador.vida_maxima}, Esquiva={jogador.esquiva}")
        print(f"Modificadores: {raca.modificadores}")

    print("\n" + "="*40)
    print("\n--- Testando combinação Raça + Vocação ---")

    # Teste de combinação
    from vocacoes.vocacao import Guerreiro

    jogador = Jogador("Aragorn")
    print(f"\nJogador base: {jogador.mostrar_status()}")

    raca = Humano()
    raca.aplicar_modificadores(jogador)

    vocacao = Guerreiro()
    vocacao.aplicar_modificadores(jogador)

    print(f"\nApós Humano + Guerreiro:")
    jogador.mostrar_status()
