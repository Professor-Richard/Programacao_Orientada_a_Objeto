class Pagamento:
    def pagar(self, valor: float) -> str:
        raise NotImplementedError


class Pix(Pagamento):
    def pagar(self, valor: float) -> str:
        return f"Pago via PIX: R$ {valor:.2f}"


class Cartao(Pagamento):
    def pagar(self, valor: float) -> str:
        return f"Pago no cartão: R$ {valor:.2f}"


class Boleto(Pagamento):
    def pagar(self, valor: float) -> str:
        return f"Gerado boleto: R$ {valor:.2f}"


def finalizar_compra(meio: Pagamento, valor: float) -> str:
    return meio.pagar(valor)
