class Espada:
    def atacar(self) -> str:
        return "Corte com espada"


class Cajado:
    def atacar(self) -> str:
        return "Magia com cajado"


class Arco:
    def atacar(self) -> str:
        return "Flecha disparada"


def executar_ataque(arma) -> str:
    # duck typing: não importa a classe, importa ter .atacar()
    return arma.atacar()
