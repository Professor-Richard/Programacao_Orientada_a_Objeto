from entities.entidade import Entidade


class Jogador(Entidade):
    def __init__(self, nome: str):
        # Valores base do jogador nível 1
        super().__init__(
            nome=nome,
            poder=3,
            defesa=2,
            vida_maxima=10,
            esquiva=2
        )

        # Atributos específicos do jogador
        self.nivel = 1
        self.experiencia = 0
        self.raca = None
        self.vocacao = None
        self.inventario = []
        self.xp_proximo_nivel = 100  # XP necessária para nível 2

    def ganhar_experiencia(self, quantidade: int):
        self.experiencia += quantidade
        print(f"{self.nome} ganhou {quantidade} XP!")

        # Verifica se subiu de nível
        if self.experiencia >= self.xp_proximo_nivel:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia -= self.xp_proximo_nivel

        # Aumenta XP necessária para próximo nível em 40%
        self.xp_proximo_nivel = int(self.xp_proximo_nivel * 1.4)

        # Aumenta atributos em 50% (arredondado para baixo)
        self.poder = int(self.poder * 1.5)
        self.defesa = int(self.defesa * 1.5)
        self.vida_maxima = int(self.vida_maxima * 1.5)
        self.esquiva = int(self.esquiva * 1.5)

        # Cura total ao subir de nível
        self.vida_atual = self.vida_maxima

        print(f"PARABÉNS! {self.nome} subiu para o nível {self.nivel}!")

    def aplicar_raca(self, modificadores: dict):
        self.poder += modificadores.get("poder", 0)
        self.defesa += modificadores.get("defesa", 0)
        self.vida_maxima += modificadores.get("vida_maxima", 0)
        self.esquiva += modificadores.get("esquiva", 0)
        self.vida_atual = self.vida_maxima

    def aplicar_vocacao(self, modificadores: dict):
        self.poder += modificadores.get("poder", 0)
        self.defesa += modificadores.get("defesa", 0)
        self.vida_maxima += modificadores.get("vida_maxima", 0)
        self.esquiva += modificadores.get("esquiva", 0)
        self.vida_atual = self.vida_maxima

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{item} adicionado ao inventário!")

    def remover_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            print(f"{item} removido do inventário!")
            return True
        return False

    def usar_item(self, indice: int):
        if 0 <= indice < len(self.inventario):
            item = self.inventario[indice]
            print(f"Usando {item}...")
            # Aqui vai a lógica de usar o item (será implementada depois)
            self.remover_item(item)
            return True
        return False

    def mostrar_status(self):
        print(f"\n=== STATUS DO JOGADOR ===")
        print(f"Nome: {self.nome}")
        print(f"Nível: {self.nivel}")
        print(f"XP: {self.experiencia}/{self.xp_proximo_nivel}")
        print(f"Vida: {self.vida_atual}/{self.vida_maxima}")
        print(f"Poder: {self.poder}")
        print(f"Defesa: {self.defesa}")
        print(f"Esquiva: {self.esquiva}")
        print(f"Raça: {self.raca}")
        print(f"Vocação: {self.vocacao}")
        print(f"Itens: {len(self.inventario)}")
        print("=========================\n")

    def mostrar_inventario(self):
        if not self.inventario:
            print("Inventário vazio.")
            return

        print("\n=== INVENTÁRIO ===")
        for i, item in enumerate(self.inventario):
            print(f"{i+1}. {item}")
        print("==================\n")


if __name__ == "__main__":
    # Teste da classe Jogador
    heroi = Jogador("Aragorn")
    heroi.mostrar_status()

    # Teste de ganho de XP
    heroi.ganhar_experiencia(50)
    heroi.mostrar_status()

    heroi.ganhar_experiencia(60)  # Deve subir de nível
    heroi.mostrar_status()

    # Teste de itens
    heroi.adicionar_item("Poção de cura")
    heroi.adicionar_item("Espada longa")
    heroi.mostrar_inventario()

    heroi.usar_item(0)
    heroi.mostrar_inventario()
