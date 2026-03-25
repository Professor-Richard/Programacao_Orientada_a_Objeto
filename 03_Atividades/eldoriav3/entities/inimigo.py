from entities.entidade import Entidade
import random


class Inimigo(Entidade):
    # Constantes para os IDs das categorias
    ID_FRACO = 1
    ID_MEDIO = 2
    ID_DIFICIL = 3
    ID_BOSS = 4

    # Dicionário com todos os tipos de inimigos organizados por ID de categoria
    TIPOS = {
        # INIMIGOS FRACOS (ID 1)
        1: [
            {"nome": "Goblin", "poder": 3, "defesa": 1,
                "vida_maxima": 8, "esquiva": 2, "exp": 50},
            {"nome": "Lobo", "poder": 4, "defesa": 0,
                "vida_maxima": 7, "esquiva": 3, "exp": 50},
            {"nome": "Bandido", "poder": 3, "defesa": 1,
                "vida_maxima": 9, "esquiva": 1, "exp": 50},
            {"nome": "Esqueleto", "poder": 3, "defesa": 2,
                "vida_maxima": 6, "esquiva": 1, "exp": 50},
            {"nome": "Cultista", "poder": 4, "defesa": 0,
                "vida_maxima": 7, "esquiva": 2, "exp": 50},
            {"nome": "Aranha Gigante", "poder": 3, "defesa": 1,
                "vida_maxima": 7, "esquiva": 4, "exp": 50},
            {"nome": "Morcego Vampiro", "poder": 3, "defesa": 0,
                "vida_maxima": 5, "esquiva": 5, "exp": 50},
            {"nome": "Slime", "poder": 2, "defesa": 3,
                "vida_maxima": 10, "esquiva": 0, "exp": 50}
        ],

        # INIMIGOS MÉDIOS (ID 2)
        2: [
            {"nome": "Orc", "poder": 5, "defesa": 2,
                "vida_maxima": 15, "esquiva": 2, "exp": 100},
            {"nome": "Morto-Vivo", "poder": 5, "defesa": 3,
                "vida_maxima": 14, "esquiva": 1, "exp": 100},
            {"nome": "Harpia", "poder": 4, "defesa": 1,
                "vida_maxima": 12, "esquiva": 5, "exp": 100},
            {"nome": "Troll da Caverna", "poder": 6, "defesa": 2,
                "vida_maxima": 18, "esquiva": 1, "exp": 100}
        ],

        # INIMIGOS DIFÍCEIS (ID 3)
        3: [
            {"nome": "Cavaleiro Negro", "poder": 7, "defesa": 4,
                "vida_maxima": 25, "esquiva": 3, "exp": 200},
            {"nome": "Necromante", "poder": 8, "defesa": 2,
                "vida_maxima": 22, "esquiva": 4, "exp": 200}
        ],

        # BOSSES (ID 4)
        4: [
            {"nome": "Dragão Vermelho", "poder": 12, "defesa": 6,
                "vida_maxima": 60, "esquiva": 5, "exp": 800},
            {"nome": "Lich Rei", "poder": 10, "defesa": 5,
                "vida_maxima": 55, "esquiva": 6, "exp": 750}
        ]
    }

    def __init__(self, id_categoria: int, indice: int = None):
        """
        Cria um inimigo baseado no ID da categoria.

        Args:
            id_categoria: 1 (fraco), 2 (medio), 3 (dificil) ou 4 (boss)
            indice: posição do inimigo na lista (se None, escolhe aleatório)
        """
        if id_categoria not in self.TIPOS:
            id_categoria = self.ID_FRACO  # valor padrão

        lista_inimigos = self.TIPOS[id_categoria]

        if indice is None:
            # Escolhe um inimigo aleatório da categoria
            indice = random.randint(0, len(lista_inimigos) - 1)
        else:
            # Garante que o índice é válido
            indice = min(indice, len(lista_inimigos) - 1)
            indice = max(0, indice)

        dados = lista_inimigos[indice]

        super().__init__(
            nome=dados["nome"],
            poder=dados["poder"],
            defesa=dados["defesa"],
            vida_maxima=dados["vida_maxima"],
            esquiva=dados["esquiva"]
        )

        self.id_categoria = id_categoria
        self.exp_concedida = dados["exp"]

    @classmethod
    def criar_por_categoria(cls, id_categoria: int):
        """Cria um inimigo aleatório de uma categoria específica"""
        return cls(id_categoria)

    @classmethod
    def criar_aleatorio(cls, nivel_jogador: int = 1):
        # Define probabilidades baseado no nível do jogador
        if nivel_jogador <= 2:
            # 80% fraco (ID 1), 20% médio (ID 2)
            categorias = [cls.ID_FRACO] * 8 + [cls.ID_MEDIO] * 2
        elif nivel_jogador <= 4:
            # 30% fraco, 50% médio, 20% difícil
            categorias = [cls.ID_FRACO] * 3 + \
                [cls.ID_MEDIO] * 5 + [cls.ID_DIFICIL] * 2
        elif nivel_jogador <= 6:
            # 50% médio, 40% difícil, 10% boss
            categorias = [cls.ID_MEDIO] * 5 + \
                [cls.ID_DIFICIL] * 4 + [cls.ID_BOSS] * 1
        else:
            # 60% difícil, 40% boss
            categorias = [cls.ID_DIFICIL] * 6 + [cls.ID_BOSS] * 4

        id_escolhido = random.choice(categorias)
        return cls(id_escolhido)

    def __str__(self):
        categoria = {1: "Fraco", 2: "Médio", 3: "Difícil",
                     4: "BOSS"}.get(self.id_categoria, "Desconhecido")
        return f"{self.nome} ({categoria}) - Vida: {self.vida_atual}/{self.vida_maxima}"


if __name__ == "__main__":
    print("=== TESTE DA CLASSE INIMIGO ===\n")

    # Teste 1: Criar inimigos por ID
    print("1. Criando inimigos por ID de categoria:")

    print("\n   ID 1 (Fracos) - 3 exemplos:")
    for i in range(3):
        inimigo = Inimigo(1)
        print(f"   - {inimigo}")

    print("\n   ID 2 (Médios):")
    inimigo = Inimigo(2)
    print(f"   - {inimigo}")

    print("\n   ID 3 (Difíceis):")
    inimigo = Inimigo(3)
    print(f"   - {inimigo}")

    print("\n   ID 4 (BOSS):")
    inimigo = Inimigo(4)
    print(f"   - {inimigo}")

    # Teste 2: Criar com índice específico
    print("\n2. Criando inimigo específico da lista (Dragão - ID 4, índice 0):")
    dragao = Inimigo(4, 0)
    print(f"   - {dragao}")

    # Teste 3: Criar aleatório baseado no nível
    print("\n3. Criando aleatórios por nível do jogador:")

    print("   Nível 1 (deve pegar muitos fracos):")
    for i in range(3):
        inimigo = Inimigo.criar_aleatorio(1)
        print(f"   - {inimigo}")

    print("\n   Nível 5 (pode pegar bosses):")
    for i in range(3):
        inimigo = Inimigo.criar_aleatorio(5)
        print(f"   - {inimigo}")

    # Teste 4: Listar todos os inimigos por categoria
    print("\n4. Todos os inimigos disponíveis:")

    categorias = {1: "FRACOS", 2: "MÉDIOS", 3: "DIFÍCEIS", 4: "BOSSES"}

    for id_cat, nome_cat in categorias.items():
        print(f"\n   {nome_cat} (ID {id_cat}):")
        for i, inimigo_data in enumerate(Inimigo.TIPOS[id_cat]):
            print(f"   - [{i}] {inimigo_data['nome']}: Poder {inimigo_data['poder']}, "
                  f"Defesa {inimigo_data['defesa']}, Vida {inimigo_data['vida_maxima']}, "
                  f"EXP {inimigo_data['exp']}")
