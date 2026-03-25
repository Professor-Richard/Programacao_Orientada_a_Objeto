
class Progressao:
    """Classe responsável por gerenciar a progressão de nível"""

    # Constantes de progressão
    XP_INICIAL_NIVEL_1 = 100  # XP necessária para o nível 2
    MULTIPLICADOR_XP = 1.4     # A cada nível, a XP necessária aumenta 40%
    MULTIPLICADOR_ATRIBUTOS = 1.5  # Atributos aumentam 50% por nível

    @staticmethod
    def xp_para_proximo_nivel(nivel_atual: int) -> int:
        """
        Calcula a quantidade de XP necessária para o próximo nível

        Args:
            nivel_atual: Nível atual do jogador

        Returns:
            int: XP necessária para o próximo nível
        """
        if nivel_atual < 1:
            nivel_atual = 1

        # Fórmula: XP = 100 * (1.4)^(nivel_atual - 1)
        xp = Progressao.XP_INICIAL_NIVEL_1 * \
            (Progressao.MULTIPLICADOR_XP ** (nivel_atual - 1))
        return int(xp)

    @staticmethod
    def xp_total_para_nivel(nivel_desejado: int) -> int:
        """
        Calcula o total de XP acumulado necessário para atingir um nível

        Args:
            nivel_desejado: Nível que se deseja atingir

        Returns:
            int: XP total acumulada necessária
        """
        if nivel_desejado <= 1:
            return 0

        xp_total = 0
        for nivel in range(1, nivel_desejado):
            xp_total += Progressao.xp_para_proximo_nivel(nivel)

        return xp_total

    @staticmethod
    def calcular_nivel_por_xp(xp_atual: int) -> int:
        """
        Calcula em qual nível um jogador está baseado na XP acumulada

        Args:
            xp_atual: XP acumulada do jogador

        Returns:
            int: Nível atual do jogador
        """
        nivel = 1
        xp_restante = xp_atual

        while xp_restante >= Progressao.xp_para_proximo_nivel(nivel):
            xp_restante -= Progressao.xp_para_proximo_nivel(nivel)
            nivel += 1

            # Limite de segurança (nível máximo 20)
            if nivel > 20:
                return 20

        return nivel

    @staticmethod
    def xp_restante_para_proximo_nivel(xp_atual: int, nivel_atual: int) -> int:
        """
        Calcula quanto XP falta para o próximo nível

        Args:
            xp_atual: XP atual do jogador
            nivel_atual: Nível atual do jogador

        Returns:
            int: XP que falta para o próximo nível
        """
        xp_necessario = Progressao.xp_para_proximo_nivel(nivel_atual)
        return max(0, xp_necessario - xp_atual)

    @staticmethod
    def calcular_novos_atributos(atributo_atual: int) -> int:
        """
        Calcula o novo valor de um atributo ao subir de nível

        Args:
            atributo_atual: Valor atual do atributo

        Returns:
            int: Novo valor do atributo (aumento de 50%, arredondado para baixo)
        """
        return int(atributo_atual * Progressao.MULTIPLICADOR_ATRIBUTOS)

    @staticmethod
    def pode_subir_nivel(xp_atual: int, nivel_atual: int) -> bool:
        """
        Verifica se o jogador tem XP suficiente para subir de nível

        Args:
            xp_atual: XP atual do jogador
            nivel_atual: Nível atual do jogador

        Returns:
            bool: True se pode subir de nível, False caso contrário
        """
        return xp_atual >= Progressao.xp_para_proximo_nivel(nivel_atual)

    @staticmethod
    def tabela_niveis(ate_nivel: int = 10):
        """
        Gera uma tabela de níveis para referência

        Args:
            ate_nivel: Até qual nível gerar a tabela

        Returns:
            dict: Dicionário com informações de cada nível
        """
        tabela = {}
        xp_acumulado = 0

        for nivel in range(1, ate_nivel + 1):
            xp_necessario = Progressao.xp_para_proximo_nivel(nivel)

            tabela[nivel] = {
                "xp_para_proximo": xp_necessario,
                "xp_acumulado_ate_nivel": xp_acumulado,
                "xp_total_ate_proximo": xp_acumulado + xp_necessario,
                "multiplicador_atributos": Progressao.MULTIPLICADOR_ATRIBUTOS ** (nivel - 1)
            }

            xp_acumulado += xp_necessario

        return tabela


class CalculadoraNivel:
    """Classe auxiliar para cálculos de balanceamento de nível"""

    @staticmethod
    def nivel_recomendado_para_desafio(xp_jogador: int, xp_recompensa: int) -> str:
        """
        Sugere se um desafio é apropriado para o nível do jogador

        Args:
            xp_jogador: XP atual do jogador
            xp_recompensa: XP que o desafio concede

        Returns:
            str: 'Fácil', 'Apropriado', 'Difícil' ou 'Perigoso'
        """
        nivel_jogador = Progressao.calcular_nivel_por_xp(xp_jogador)
        xp_necessario = Progressao.xp_para_proximo_nivel(nivel_jogador)

        proporcao = xp_recompensa / xp_necessario

        if proporcao < 0.3:
            return "Fácil"
        elif proporcao < 0.7:
            return "Apropriado"
        elif proporcao < 1.2:
            return "Difícil"
        else:
            return "Perigoso"

    @staticmethod
    def quantos_combates_para_subir_nivel(xp_por_combate: int, nivel_atual: int) -> int:
        """
        Calcula quantos combates são necessários para subir de nível

        Args:
            xp_por_combate: Média de XP ganha por combate
            nivel_atual: Nível atual do jogador

        Returns:
            int: Número aproximado de combates necessários
        """
        xp_necessario = Progressao.xp_para_proximo_nivel(nivel_atual)

        if xp_por_combate <= 0:
            return float('inf')

        import math
        return math.ceil(xp_necessario / xp_por_combate)


if __name__ == "__main__":
    print("=== SISTEMA DE PROGRESSÃO ===\n")

    # Teste 1: Tabela de níveis
    print("1. TABELA DE NÍVEIS (1-10):")
    print("-" * 60)
    print(f"{'Nível':<6} {'XP p/ próximo':<15} {'XP acumulado':<15} {'Multiplicador':<15}")
    print("-" * 60)

    tabela = Progressao.tabela_niveis(10)
    for nivel, dados in tabela.items():
        print(f"{nivel:<6} {dados['xp_para_proximo']:<15} {dados['xp_acumulado_ate_nivel']:<15} "
              f"{dados['multiplicador_atributos']:.2f}x")

    print("\n" + "="*60)

    # Teste 2: Cálculo de nível por XP
    print("\n2. CÁLCULO DE NÍVEL POR XP:")
    testes_xp = [0, 50, 100, 250, 500, 1000, 2000, 5000]

    for xp in testes_xp:
        nivel = Progressao.calcular_nivel_por_xp(xp)
        print(f"XP {xp:4} → Nível {nivel}")

    print("\n" + "="*60)

    # Teste 3: Progressão de atributos
    print("\n3. PROGRESSÃO DE ATRIBUTOS (valor base 10):")
    atributo_base = 10

    for nivel in range(1, 6):
        multiplicador = Progressao.MULTIPLICADOR_ATRIBUTOS ** (nivel - 1)
        valor = int(atributo_base * multiplicador)
        print(f"Nível {nivel}: {valor} (multiplicador {multiplicador:.2f}x)")

    print("\n" + "="*60)

    # Teste 4: Balanceamento de desafios
    print("\n4. BALANCEAMENTO DE DESAFIOS:")
    print("Jogador nível 3 (XP ≈ 240):")

    desafios = [
        ("Goblin (50 XP)", 50),
        ("Orc (100 XP)", 100),
        ("Cavaleiro Negro (200 XP)", 200),
        ("Dragão (800 XP)", 800)
    ]

    for nome, xp in desafios:
        dificuldade = CalculadoraNivel.nivel_recomendado_para_desafio(240, xp)
        print(f"  {nome}: {dificuldade}")

    print("\n" + "="*60)

    # Teste 5: Combates necessários para subir de nível
    print("\n5. COMBATES PARA SUBIR DE NÍVEL:")

    for nivel in range(1, 6):
        xp_necessario = Progressao.xp_para_proximo_nivel(nivel)
        print(f"\nNível {nivel} → {nivel+1} (precisa de {xp_necessario} XP):")

        # Diferentes tipos de inimigos
        goblins = CalculadoraNivel.quantos_combates_para_subir_nivel(50, nivel)
        orcs = CalculadoraNivel.quantos_combates_para_subir_nivel(100, nivel)
        dragoes = CalculadoraNivel.quantos_combates_para_subir_nivel(
            800, nivel)

        print(f"  Só matar Goblins (50 XP): {goblins} combates")
        print(f"  Só matar Orcs (100 XP): {orcs} combates")
        print(f"  Só matar Dragões (800 XP): {dragoes} combates")
