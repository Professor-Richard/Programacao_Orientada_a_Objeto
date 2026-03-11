# Exemplo BANCO
class ContaBanco:
    def __init__(self, titular, n_conta):
        self.saldo = 0
        self.titular = titular
        self.n_conta = n_conta
        self.senha = "1234"

    def exibir(self):
        print(f"Titular: {self.titular}")
        print(f"Número da Conta: {self.n_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")


def entrada():
    nome = input("Digite seu primeiro nome: ").strip().lower()
    conta = input("Digite os 4 números da sua conta: ").strip()
    return nome, conta


def validacao(nome, conta, banco):
    if nome == banco.titular and conta == banco.n_conta:
        senha = input("Digite sua senha: ").strip()
        if senha == banco.senha:
            print("Acesso permitido! Bem-vindo ao banco.")
            return True
        else:
            print("Senha incorreta!")
    else:
        print("Nome ou número da conta inválido.")
    return False


banco = ContaBanco("richard", "1234")

nome, conta = entrada()
if validacao(nome, conta, banco):
    banco.exibir()
    banco.depositar(100)
    banco.sacar(50)
    banco.exibir()
