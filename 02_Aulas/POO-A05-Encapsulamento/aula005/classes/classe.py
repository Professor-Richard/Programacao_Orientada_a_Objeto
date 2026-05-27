#classes
from rich import print
from rich.panel import Panel
class Conta:
  def __init__(self,nome,saldo):
    self.nome=nome
    self.__saldo=saldo
  
  @property
  def get_mostrar_saldo(self): 
    mensagem= f'Usuario: [yellow]{self.nome}[/yellow]'
    mensagem+=f'\nSaldo atual: [green]R${self.__saldo:.2f}[/]'
    caixa=Panel(mensagem,title="[red]BANCK IN TERMINAL",width=30)
    print(caixa)
    return f'{caixa}'
  
  @get_mostrar_saldo.setter
  def set_alterar_saldo(self,valor):
    self.__saldo += valor
    return self.__saldo