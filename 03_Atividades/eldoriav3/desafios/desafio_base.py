import random
from sistema.dados import rolar_d20


class DesafioBase:
    """Classe base para todos os desafios"""

    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao

    def executar(self, jogador):
        """Método a ser implementado por cada desafio"""
        raise NotImplementedError(
            "Cada desafio deve implementar seu próprio método executar")

    def __str__(self):
        return f"{self.nome}: {self.descricao}"


class DesafioBau(DesafioBase):
    """
    Desafio de abrir um baú com 3 tentativas
    Dificuldades: Fácil (5+), Médio (10+), Difícil (15+)
    """

    # IDs das dificuldades
    ID_FACIL = 1
    ID_MEDIO = 2
    ID_DIFICIL = 3

    # Dicionário com as dificuldades do baú
    DIFICULDADES = {
        1: {  # Fácil
            "nome": "Baú Simples",
            "descricao": "Um baú velho e enferrujado, parece fácil de abrir",
            "dificuldade": 5,
            "recompensa": "Poção Pequena",
            "recompensa_exp": 20
        },
        2: {  # Médio
            "nome": "Baú Reforçado",
            "descricao": "Um baú de madeira nobre com fechadura resistente",
            "dificuldade": 10,
            "recompensa": "Poção de Cura",
            "recompensa_exp": 50
        },
        3: {  # Difícil
            "nome": "Baú Élfico",
            "descricao": "Um baú antigo com mecanismos complexos e runas de proteção",
            "dificuldade": 15,
            "recompensa": "Poção Grande",
            "recompensa_exp": 100
        }
    }

    def __init__(self, id_dificuldade: int):
        """
        Cria um desafio de baú baseado na dificuldade

        Args:
            id_dificuldade: 1 (fácil), 2 (médio) ou 3 (difícil)
        """
        if id_dificuldade not in self.DIFICULDADES:
            id_dificuldade = self.ID_FACIL

        dados = self.DIFICULDADES[id_dificuldade]

        super().__init__(
            nome=dados["nome"],
            descricao=dados["descricao"]
        )

        self.id_dificuldade = id_dificuldade
        self.dificuldade = dados["dificuldade"]
        self.recompensa = dados["recompensa"]
        self.recompensa_exp = dados["recompensa_exp"]
        self.tentativas_restantes = 3
        self.aberto = False

    def executar(self, jogador):
        """
        Executa o desafio do baú

        Args:
            jogador: Objeto do jogador tentando abrir o baú

        Returns:
            dict: Resultado do desafio
        """
        print(f"\n{self.nome}")
        print(self.descricao)
        print(
            f"Dificuldade: {self.dificuldade} (precisa tirar {self.dificuldade} ou mais no D20)")
        print(f"Tentativas: {self.tentativas_restantes}")
        print(f"Recompensa: {self.recompensa} + {self.recompensa_exp} XP")

        while self.tentativas_restantes > 0 and not self.aberto:
            print(f"\n--- Tentativa {4 - self.tentativas_restantes}/3 ---")
            input("Pressione ENTER para rolar o D20...")

            # Rola o dado
            rolagem = rolar_d20()
            print(f"Rolou: {rolagem}")

            # Verifica se conseguiu abrir
            if rolagem >= self.dificuldade:
                print(f"SUCESSO! Você conseguiu abrir o baú!")
                self.aberto = True

                # Adiciona recompensa ao jogador
                jogador.adicionar_item(self.recompensa)
                jogador.ganhar_experiencia(self.recompensa_exp)

                return {
                    "resultado": "sucesso",
                    "exp": self.recompensa_exp,
                    "recompensa": self.recompensa,
                    "mensagem": f"Você abriu o baú! Ganhou {self.recompensa} e {self.recompensa_exp} XP!"
                }
            else:
                self.tentativas_restantes -= 1
                print(f"FALHA! Não conseguiu abrir.")

                if self.tentativas_restantes > 0:
                    print(f"Tentativas restantes: {self.tentativas_restantes}")

        # Se acabaram as tentativas
        if not self.aberto:
            print("\nVocê não conseguiu abrir o baú...")
            return {
                "resultado": "falha",
                "exp": 0,
                "recompensa": None,
                "mensagem": "Suas tentativas acabaram. O baú permanece fechado."
            }

    @classmethod
    def criar_aleatorio(cls):
        """Cria um baú de dificuldade aleatória"""
        id_escolhido = random.choice(
            [cls.ID_FACIL, cls.ID_MEDIO, cls.ID_DIFICIL])
        return cls(id_escolhido)

    @classmethod
    def criar_por_nivel(cls, nivel_jogador: int):
        """
        Cria um baú baseado no nível do jogador

        Args:
            nivel_jogador: Nível atual do jogador
        """
        if nivel_jogador <= 2:
            # 60% fácil, 30% médio, 10% difícil
            ids = [cls.ID_FACIL] * 6 + [cls.ID_MEDIO] * \
                3 + [cls.ID_DIFICIL] * 1
        elif nivel_jogador <= 4:
            # 30% fácil, 50% médio, 20% difícil
            ids = [cls.ID_FACIL] * 3 + [cls.ID_MEDIO] * \
                5 + [cls.ID_DIFICIL] * 2
        else:
            # 20% fácil, 40% médio, 40% difícil
            ids = [cls.ID_FACIL] * 2 + [cls.ID_MEDIO] * \
                4 + [cls.ID_DIFICIL] * 4

        id_escolhido = random.choice(ids)
        return cls(id_escolhido)


# Dicionário com todos os tipos de desafios (para fácil acesso)
DESAFIOS = {
    "bau": DesafioBau,
    # Aqui podem ser adicionados outros desafios no futuro:
    # "armadilha": DesafioArmadilha,
    # "enigma": DesafioEnigma,
    # "santuario": DesafioSantuario,
}


def criar_desafio(tipo: str, **kwargs):
    """
    Factory function para criar desafios

    Args:
        tipo: Tipo do desafio ("bau", etc)
        **kwargs: Argumentos específicos do desafio
    """
    tipo = tipo.lower().strip()

    if tipo in DESAFIOS:
        return DESAFIOS[tipo](**kwargs)
    else:
        print(
            f"Desafio '{tipo}' não encontrado. Usando baú fácil como padrão.")
        return DesafioBau(DesafioBau.ID_FACIL)


if __name__ == "__main__":
    from entities.jogador import Jogador

    print("=== TESTE DO DESAFIO DO BAÚ ===\n")

    # Cria jogador de teste
    heroi = Jogador("Aragorn")
    print(f"Jogador: {heroi.nome}")
    print(f"XP inicial: {heroi.experiencia}")
    print(f"Itens iniciais: {heroi.inventario}")

    print("\n" + "="*50)

    # Teste 1: Baú fácil
    print("\n1. TESTE: BAÚ FÁCIL")
    print("-" * 30)

    bau_facil = DesafioBau(DesafioBau.ID_FACIL)
    resultado = bau_facil.executar(heroi)
    print(f"\nResultado: {resultado['mensagem']}")

    print("\n" + "="*50)

    # Teste 2: Baú médio
    print("\n2. TESTE: BAÚ MÉDIO")
    print("-" * 30)

    bau_medio = DesafioBau(DesafioBau.ID_MEDIO)
    resultado = bau_medio.executar(heroi)
    print(f"\nResultado: {resultado['mensagem']}")

    print("\n" + "="*50)

    # Teste 3: Baú difícil
    print("\n3. TESTE: BAÚ DIFÍCIL")
    print("-" * 30)

    bau_dificil = DesafioBau(DesafioBau.ID_DIFICIL)
    resultado = bau_dificil.executar(heroi)
    print(f"\nResultado: {resultado['mensagem']}")

    print("\n" + "="*50)

    # Teste 4: Baú aleatório por nível
    print("\n4. TESTE: BAÚS ALEATÓRIOS POR NÍVEL")
    print("-" * 30)

    niveis = [1, 3, 5]
    for nivel in niveis:
        print(f"\nNível do jogador: {nivel}")
        bau = DesafioBau.criar_por_nivel(nivel)
        print(f"  Baú gerado: {bau.nome} (dificuldade {bau.dificuldade})")

    print("\n" + "="*50)

    # Status final do jogador
    print("\nSTATUS FINAL DO JOGADOR:")
    print(f"XP: {heroi.experiencia}")
    print(f"Itens: {heroi.inventario}")
