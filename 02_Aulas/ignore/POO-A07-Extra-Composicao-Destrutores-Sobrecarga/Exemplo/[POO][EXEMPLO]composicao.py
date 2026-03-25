"""
Tema: Composição (relação "tem um") em Python

Conceitos reunidos:
- Um objeto "contém" outro objeto como atributo
- Delegação de responsabilidade
- Troca de componente em tempo de execução (mais flexível que herança)
"""
# ----------------------------
# Exemplo 1: Carro TEM um Motor (composição forte)
# ----------------------------
class Motor:
    def __init__(self, potencia_cv: int):
        self.potencia_cv = potencia_cv

    def ligar(self) -> str:
        return f"Motor {self.potencia_cv}cv ligado"


class Carro:
    def __init__(self, modelo: str, potencia_cv: int):
        self.modelo = modelo
        self.motor = Motor(potencia_cv)  # composição: Carro TEM um Motor

    def ligar(self) -> str:
        # delegação
        return f"{self.modelo}: {self.motor.ligar()}"


# ----------------------------
# Exemplo 2: Personagem TEM uma Arma (componente injetado e trocável)
# ----------------------------
class Arma:
    def atacar(self) -> str:
        return "Ataque genérico"


class Espada(Arma):
    def atacar(self) -> str:
        return "Corte com espada"


class Arco(Arma):
    def atacar(self) -> str:
        return "Disparo de flecha"


class Personagem:
    def __init__(self, nome: str, arma: Arma):
        self.nome = nome
        self.arma = arma  # composição (agregação): arma pode ser trocada

    def atacar(self) -> str:
        return f"{self.nome}: {self.arma.atacar()}"

    def trocar_arma(self, nova_arma: Arma) -> None:
        self.arma = nova_arma


# ----------------------------
# Exemplo 3: Pedido TEM Itens (lista de objetos)
# ----------------------------
class Item:
    def __init__(self, nome: str, preco: float, quantidade: int = 1):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return self.preco * self.quantidade


class Pedido:
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.itens: list[Item] = []

    def adicionar_item(self, item: Item) -> None:
        self.itens.append(item)

    def total(self) -> float:
        return sum(item.subtotal() for item in self.itens)

    def resumo(self) -> str:
        linhas = [f"Pedido de {self.cliente}"]
        for i in self.itens:
            linhas.append(f"- {i.nome} x{i.quantidade} = R$ {i.subtotal():.2f}")
        linhas.append(f"TOTAL = R$ {self.total():.2f}")
        return "\n".join(linhas)


def main() -> None:
    print("\n=== Exemplo 1: Carro TEM Motor ===")
    carro = Carro("Fusca", 65)
    print(carro.ligar())

    print("\n=== Exemplo 2: Personagem TEM Arma (troca em runtime) ===")
    p = Personagem("Fabim", Espada())
    print(p.atacar())
    p.trocar_arma(Arco())
    print(p.atacar())

    print("\n=== Exemplo 3: Pedido TEM Itens ===")
    pedido = Pedido("Cliente A")
    pedido.adicionar_item(Item("Mouse", 80.0, 1))
    pedido.adicionar_item(Item("Teclado", 150.0, 1))
    pedido.adicionar_item(Item("Cabo HDMI", 25.0, 2))
    print(pedido.resumo())


if __name__ == "__main__":
    main()
