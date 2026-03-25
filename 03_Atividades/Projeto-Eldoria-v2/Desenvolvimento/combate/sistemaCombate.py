from sistema_dado.dados import SistemaDeDados


class Combate:
    def __init__(self, combatente1, combatente2):
        self.combatente1 = combatente1
        self.combatente2 = combatente2
        self.turno_atual = combatente1

    def alternar_turno(self):
        if self.turno_atual == self.combatente1:
            self.turno_atual = self.combatente2
        else:
            self.turno_atual = self.combatente1

    def calcular_dano(self, atacante, defensor, critico=False):
        dano = max(1, atacante.ataque +
                   SistemaDeDados.rolar_d6() - defensor.defesa)

        if critico:
            dano *= 2

        return dano

    def resolver_ataque(self, atacante, defensor):
        rolagem = SistemaDeDados.rolar_d20()
        total_ataque = rolagem + atacante.ataque
        defesa_alvo = defensor.defesa + 10

        critico = rolagem == 20

        if critico or total_ataque >= defesa_alvo:
            dano = self.calcular_dano(atacante, defensor, critico)
            defensor.receber_dano(dano)

            return {
                "acertou": True,
                "critico": critico,
                "rolagem": rolagem,
                "total_ataque": total_ataque,
                "dano": dano,
                "vida_restante_alvo": defensor.vida_atual,
                "mensagem": (
                    f"{atacante.nome} atacou {defensor.nome} e causou {dano} de dano!"
                    if not critico
                    else f"{atacante.nome} acertou um CRÍTICO em {defensor.nome} e causou {dano} de dano!"
                )
            }

        return {
            "acertou": False,
            "critico": False,
            "rolagem": rolagem,
            "total_ataque": total_ataque,
            "dano": 0,
            "vida_restante_alvo": defensor.vida_atual,
            "mensagem": f"{atacante.nome} errou o ataque em {defensor.nome}."
        }

    def resolver_fuga(self, personagem):
        rolagem = SistemaDeDados.rolar_d20()
        total_fuga = rolagem + personagem.esquiva
        conseguiu_fugir = total_fuga >= 15

        return {
            "fugiu": conseguiu_fugir,
            "rolagem": rolagem,
            "total_fuga": total_fuga,
            "mensagem": (
                f"{personagem.nome} conseguiu fugir do combate!"
                if conseguiu_fugir
                else f"{personagem.nome} tentou fugir, mas falhou."
            )
        }

    def combate_ativo(self):
        return self.combatente1.esta_vivo() and self.combatente2.esta_vivo()

    def obter_oponente(self):
        if self.turno_atual == self.combatente1:
            return self.combatente2
        return self.combatente1

    def executar_turno_ataque(self):
        atacante = self.turno_atual
        defensor = self.obter_oponente()

        resultado = self.resolver_ataque(atacante, defensor)

        if defensor.esta_vivo():
            self.alternar_turno()

        return resultado

    def executar_turno_fuga(self):
        personagem = self.turno_atual
        resultado = self.resolver_fuga(personagem)

        if not resultado["fugiu"]:
            self.alternar_turno()

        return resultado

    def obter_vencedor(self):
        if self.combatente1.esta_vivo() and not self.combatente2.esta_vivo():
            return self.combatente1
        if self.combatente2.esta_vivo() and not self.combatente1.esta_vivo():
            return self.combatente2
        return None
