class Conta:
  def __init__(self,nome,saldo):
    self.nome=nome #publico
    self.__saldo=saldo #privado

  def __str__(self):
    return f'Usuario: {self.nome}\nSaldo atual: R${self.__saldo:.2f}'  
  
  @property
  def get_mostrar_saldo(self):
    return f'Usuario: {self.nome}\nSaldo atual: R${self.__saldo:.2f}'  

  @get_mostrar_saldo.setter
  def set_alterar_saldo(self,valor):
    self.__saldo+=valor
    print(f'{self.__saldo:.2f}')