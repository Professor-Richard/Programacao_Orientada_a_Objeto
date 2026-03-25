import os
import random
from entities.jogador import Jogador
from entities.inimigo import Inimigo
from classes.classes import criar_raca, listar_racas
from vocacoes.vocacao import criar_vocacao, listar_vocacoes
from sistema.combate import Combate
from sistema.progressao import Progressao
from desafios.desafio_base import DesafioBau


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_titulo():
    """Mostra o título do jogo"""
    print("=" * 60)
    print("                    ELDORIA RPG")
    print("=" * 60)


def pausar():
    """Pausa a execução até o usuário pressionar ENTER"""
    input("\nPressione ENTER para continuar...")


def criar_personagem():
    """Cria um novo personagem"""
    limpar_tela()
    mostrar_titulo()

    print("\n=== CRIAÇÃO DE PERSONAGEM ===\n")

    # Nome do personagem
    nome = input("Digite o nome do seu herói: ").strip()
    if not nome:
        nome = "Aragorn"
        print(f"Nome vazio. Usando {nome}.")

    # Cria o jogador
    jogador = Jogador(nome)

    # Escolha da raça
    print("\n--- RAÇAS DISPONÍVEIS ---")
    racas = listar_racas()
    for i, raca in enumerate(racas, 1):
        print(f"{i}. {raca.capitalize()}")

    while True:
        try:
            escolha = input("\nEscolha sua raça (número): ").strip()
            indice = int(escolha) - 1
            if 0 <= indice < len(racas):
                raca_escolhida = racas[indice]
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

    # Aplica a raça
    raca = criar_raca(raca_escolhida)
    raca.aplicar_modificadores(jogador)
    jogador.raca = raca.nome

    # Escolha da vocação
    print("\n--- VOCAÇÕES DISPONÍVEIS ---")
    vocacoes = listar_vocacoes()
    for i, voc in enumerate(vocacoes, 1):
        print(f"{i}. {voc.capitalize()}")

    while True:
        try:
            escolha = input("\nEscolha sua vocação (número): ").strip()
            indice = int(escolha) - 1
            if 0 <= indice < len(vocacoes):
                voc_escolhida = vocacoes[indice]
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

    # Aplica a vocação
    vocacao = criar_vocacao(voc_escolhida)
    vocacao.aplicar_modificadores(jogador)
    jogador.vocacao = vocacao.nome

    # Itens iniciais
    jogador.adicionar_item("Poção de Cura")
    jogador.adicionar_item("Poção de Cura")

    print("\nPersonagem criado com sucesso!")
    jogador.mostrar_status()
    pausar()

    return jogador


def menu_principal():
    """Exibe o menu principal"""
    limpar_tela()
    mostrar_titulo()

    print("\n1. Novo Jogo")
    print("2. Sair")

    while True:
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            return "novo"
        elif opcao == "2":
            return "sair"
        else:
            print("Opção inválida. Digite 1 ou 2.")


def menu_acao():
    """Menu de ações durante o jogo"""
    print("\n=== O QUE DESEJA FAZER? ===")
    print("1. Explorar (procurar inimigos)")
    print("2. Procurar baús")
    print("3. Ver status do personagem")
    print("4. Ver inventário")
    print("5. Descansar (recupera 20% da vida)")
    print("6. Sair do jogo")

    while True:
        opcao = input("\nEscolha uma ação: ").strip()

        if opcao in ["1", "2", "3", "4", "5", "6"]:
            return opcao
        else:
            print("Opção inválida. Digite um número de 1 a 6.")


def explorar(jogador):
    """Exploração - encontra inimigos aleatórios"""
    limpar_tela()
    print("\n=== EXPLORANDO ===\n")

    # Chance de encontrar inimigo (80%)
    if random.random() < 0.8:
        print("Você encontrou um inimigo!")

        # Cria inimigo baseado no nível do jogador
        inimigo = Inimigo.criar_aleatorio(jogador.nivel)
        # Pega o nome da categoria baseado no id
        categorias = {1: "Fraco", 2: "Médio", 3: "Difícil", 4: "BOSS"}
        nome_categoria = categorias.get(inimigo.id_categoria, "Desconhecido")
        print(f"\n Apareceu: {inimigo.nome} (nível {nome_categoria})")

        # Inicia combate
        combate = Combate(jogador, inimigo)
        resultado = combate.iniciar()

        print(f"\n{resultado['mensagem']}")

        # Se venceu, ganha XP
        if resultado["resultado"] == "vitoria":
            jogador.ganhar_experiencia(resultado["exp"])

        # Se morreu, retorna False
        if resultado["resultado"] == "derrota":
            return False
    else:
        print("Nada encontrado por aqui...")

    pausar()
    return True


def procurar_baus(jogador):
    """Procura e tenta abrir baús"""
    limpar_tela()
    print("\n=== PROCURANDO BAÚS ===\n")

    # Chance de encontrar baú (60%)
    if random.random() < 0.6:
        print("Você encontrou um baú misterioso!")

        # Cria baú baseado no nível do jogador
        bau = DesafioBau.criar_por_nivel(jogador.nivel)
        resultado = bau.executar(jogador)

        print(f"\n{resultado['mensagem']}")
    else:
        print("Não encontrou nenhum baú...")

    pausar()
    return True


def descansar(jogador):
    """Descansa e recupera parte da vida"""
    limpar_tela()
    print("\n=== DESCANSANDO ===\n")

    cura = int(jogador.vida_maxima * 0.2)  # 20% da vida máxima
    cura_real = jogador.curar(cura)

    print(f"Você descansou e recuperou {cura_real} pontos de vida!")
    print(f"Vida atual: {jogador.vida_atual}/{jogador.vida_maxima}")

    pausar()
    return True


def jogo_principal(jogador):
    """Loop principal do jogo"""
    jogando = True

    while jogando:
        limpar_tela()
        mostrar_titulo()

        # Mostra status resumido
        print(f"\n{jogador.nome} | Nível {jogador.nivel} | "
              f"Vida: {jogador.vida_atual}/{jogador.vida_maxima} | "
              f"XP: {jogador.experiencia}/{jogador.xp_proximo_nivel}")

        opcao = menu_acao()

        if opcao == "1":
            jogando = explorar(jogador)
        elif opcao == "2":
            jogando = procurar_baus(jogador)
        elif opcao == "3":
            limpar_tela()
            jogador.mostrar_status()
            pausar()
        elif opcao == "4":
            limpar_tela()
            jogador.mostrar_inventario()
            pausar()
        elif opcao == "5":
            jogando = descansar(jogador)
        elif opcao == "6":
            print("\nAté logo, aventureiro!")
            return False

        # Verifica se o jogador morreu
        if not jogador.esta_vivo():
            print("\nVOCÊ MORREU!")
            print("Fim de jogo.")
            pausar()
            return False

    return True


def main():
    """Função principal do jogo"""
    while True:
        opcao = menu_principal()

        if opcao == "novo":
            jogador = criar_personagem()
            continuar = jogo_principal(jogador)

            if not continuar:
                print("\nVoltando ao menu principal...")
                pausar()

        elif opcao == "sair":
            print("\nObrigado por jogar Eldoria! Até a próxima.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nJogo interrompido pelo usuário. Até mais!")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
        print("Reiniciando o jogo...")
        pausar()
        main()
