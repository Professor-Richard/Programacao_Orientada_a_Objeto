
import random
from sistema.dados import rolar_d20, rolar_d6


class Combate:
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo
        self.turno = 0
        self.em_andamento = True
        self.vitoria = False
        self.fugiu = False

    def iniciar(self):
        """Inicia o combate e retorna o resultado"""
        print(f"\nCOMBATE: {self.jogador.nome} vs {self.inimigo.nome}")
        print(
            f"{self.jogador.nome}: Vida {self.jogador.vida_atual}/{self.jogador.vida_maxima}")
        print(
            f"{self.inimigo.nome}: Vida {self.inimigo.vida_atual}/{self.inimigo.vida_maxima}")

        # Decide quem começa (maior esquiva)
        jogador_iniciativa = rolar_d20() + self.jogador.esquiva
        inimigo_iniciativa = rolar_d20() + self.inimigo.esquiva

        if jogador_iniciativa >= inimigo_iniciativa:
            print(f"{self.jogador.nome} começa atacando!")
            self.turno_jogador = True
        else:
            print(f"{self.inimigo.nome} começa atacando!")
            self.turno_jogador = False

        # Loop principal do combate
        while self.em_andamento:
            self.exibir_status()

            if self.turno_jogador:
                self.turno_do_jogador()
            else:
                self.turno_do_inimigo()

            # Verifica condições de fim de combate
            self.verificar_fim_combate()

            # Alterna turno
            self.turno_jogador = not self.turno_jogador
            self.turno += 1

        # Retorna resultado
        return self.resultado()

    def turno_do_jogador(self):
        """Gerencia o turno do jogador"""
        print(f"\n--- SEU TURNO ---")

        while True:
            print("\nEscolha uma ação:")
            print("1. Atacar")
            print("2. Usar Poção")
            print("3. Tentar Fugir")

            escolha = input("Digite o número da ação: ").strip()

            if escolha == "1":
                self.acao_atacar(self.jogador, self.inimigo)
                break
            elif escolha == "2":
                if self.acao_usar_pocao():
                    break
                else:
                    print("Você não tem poções! Escolha outra ação.")
            elif escolha == "3":
                self.acao_fugir()
                break
            else:
                print("Opção inválida! Tente novamente.")

    def turno_do_inimigo(self):
        """Gerencia o turno do inimigo"""
        print(f"\n--- TURNO DO {self.inimigo.nome.upper()} ---")
        self.acao_atacar(self.inimigo, self.jogador)

    def acao_atacar(self, atacante, defensor):
        """Resolve uma ação de ataque"""
        print(f"{atacante.nome} ataca!")

        # Rola o ataque
        ataque_roll = rolar_d20()
        ataque_total = ataque_roll + atacante.poder

        # Defesa do alvo
        defesa_alvo = defensor.defesa + 10

        print(
            f"{atacante.nome} rolou {ataque_roll} + {atacante.poder} = {ataque_total}")
        print(f"Defesa de {defensor.nome}: {defesa_alvo}")

        # Verifica crítico (20 natural)
        if ataque_roll == 20:
            print("ACERTO CRÍTICO!")
            dano = self.calcular_dano(atacante, defensor, critico=True)
            print(f"{defensor.nome} sofreu {dano} de dano!")
            defensor.receber_dano(dano)

        # Verifica falha crítica (1 natural)
        elif ataque_roll == 1:
            print("FALHA CRÍTICA! O ataque errou feio!")

        # Verifica se acertou
        elif ataque_total >= defesa_alvo:
            print("Ataque bem-sucedido!")
            dano = self.calcular_dano(atacante, defensor)
            print(f"{defensor.nome} sofreu {dano} de dano!")
            defensor.receber_dano(dano)

        else:
            print("Ataque errou!")

    def calcular_dano(self, atacante, defensor, critico=False):
        """Calcula o dano de um ataque"""
        # Rola o dado de dano (d6)
        dado_dano = rolar_d6()

        # Dano base: poder + dado
        dano_base = atacante.poder + dado_dano

        # Subtrai a defesa
        dano_final = dano_base - defensor.defesa

        # Dano mínimo de 1
        dano_final = max(1, dano_final)

        # Se for crítico, dobra o dano
        if critico:
            dano_final *= 2
            print(
                f"Dano crítico! {dano_base} - {defensor.defesa} = {dano_final//2} x2 = {dano_final}")
        else:
            print(
                f"Dano: {atacante.poder} + {dado_dano} - {defensor.defesa} = {dano_final}")

        return dano_final

    def acao_usar_pocao(self):
        """Tenta usar uma poção"""
        # Procura poção no inventário
        pocao_encontrada = None
        for i, item in enumerate(self.jogador.inventario):
            if "poção" in item.lower() or "pocao" in item.lower():
                pocao_encontrada = i
                break

        if pocao_encontrada is not None:
            self.jogador.usar_item(pocao_encontrada)
            return True
        else:
            return False

    def acao_fugir(self):
        """Tenta fugir do combate"""
        print(f"{self.jogador.nome} tenta fugir!")

        # Teste de fuga: d20 + esquiva >= 15
        fuga_roll = rolar_d20()
        fuga_total = fuga_roll + self.jogador.esquiva

        print(
            f"{self.jogador.nome} rolou {fuga_roll} + {self.jogador.esquiva} = {fuga_total}")

        if fuga_total >= 15:
            print("Fuga bem-sucedida!")
            self.em_andamento = False
            self.fugiu = True
        else:
            print("Falhou ao fugir! O inimigo ataca!")
            # O inimigo ganha um ataque gratuito
            self.acao_atacar(self.inimigo, self.jogador)

    def verificar_fim_combate(self):
        """Verifica se o combate deve terminar"""
        if not self.jogador.esta_vivo():
            print(f"\n{self.jogador.nome} foi derrotado!")
            self.em_andamento = False
            self.vitoria = False

        elif not self.inimigo.esta_vivo():
            print(f"\n{self.inimigo.nome} foi derrotado!")
            self.em_andamento = False
            self.vitoria = True

    def exibir_status(self):
        """Exibe o status atual do combate"""
        print(f"\n--- STATUS ---")
        print(
            f"{self.jogador.nome}: {self.jogador.vida_atual}/{self.jogador.vida_maxima}")
        print(
            f"{self.inimigo.nome}: {self.inimigo.vida_atual}/{self.inimigo.vida_maxima}")
        print(f"Turno: {self.turno + 1}")

    def resultado(self):
        """Retorna o resultado do combate"""
        if self.fugiu:
            return {
                "resultado": "fugiu",
                "exp": 0,
                "mensagem": f"{self.jogador.nome} fugiu do combate!"
            }
        elif self.vitoria:
            return {
                "resultado": "vitoria",
                "exp": self.inimigo.exp_concedida,
                "mensagem": f"Vitória! Ganhou {self.inimigo.exp_concedida} XP!"
            }
        else:
            return {
                "resultado": "derrota",
                "exp": 0,
                "mensagem": f"{self.jogador.nome} foi derrotado..."
            }


def simular_combate_rapido(jogador, inimigo):
    """Função auxiliar para criar e iniciar um combate rapidamente"""
    combate = Combate(jogador, inimigo)
    return combate.iniciar()


if __name__ == "__main__":
    from entities.jogador import Jogador
    from entities.inimigo import Inimigo

    print("=== TESTE DO SISTEMA DE COMBATE ===\n")

    # Cria jogador de teste
    heroi = Jogador("Aragorn")
    heroi.vida_atual = heroi.vida_maxima  # Garante vida cheia

    # Adiciona uma poção de teste
    heroi.adicionar_item("Poção de cura")

    print(f"Jogador: {heroi.nome}")
    print(f"Vida: {heroi.vida_atual}/{heroi.vida_maxima}")
    print(
        f"Poder: {heroi.poder}, Defesa: {heroi.defesa}, Esquiva: {heroi.esquiva}")

    # Teste com inimigo fraco
    print("\n" + "="*50)
    print("COMBATE 1: CONTRA GOBLIN")
    print("="*50)

    goblin = Inimigo.criar_por_categoria(1)  # Categoria 1 = fraco
    resultado = simular_combate_rapido(heroi, goblin)
    print(f"\nResultado: {resultado['mensagem']}")

    if resultado['resultado'] == 'vitoria':
        heroi.ganhar_experiencia(resultado['exp'])

    # Se o jogador sobreviveu, testa com inimigo mais forte
    if heroi.esta_vivo():
        print("\n" + "="*50)
        print("COMBATE 2: CONTRA ORC")
        print("="*50)

        # Cura o jogador
        heroi.curar(heroi.vida_maxima)

        orc = Inimigo("Orc")  # Pega Orc específico
        resultado = simular_combate_rapido(heroi, orc)
        print(f"\nResultado: {resultado['mensagem']}")

        if resultado['resultado'] == 'vitoria':
            heroi.ganhar_experiencia(resultado['exp'])

    # Status final
    print("\n" + "="*50)
    print("STATUS FINAL DO JOGADOR:")
    heroi.mostrar_status()
