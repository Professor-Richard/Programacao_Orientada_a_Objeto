class Conta:
  def __init__(self,nome,saldo):
    self.nome=nome
    self.__saldo=saldo

  @property  
  def mostar_saldo(self):
    # print(f'-print- Saldo atual {self.saldo}')
    return self.__saldo
  
  @mostar_saldo.setter
  def mostar_saldo(self,valor):
    self.__saldo=valor
    return self.__saldo
    # if valor>0:
    #   self.saldo+=valor
    #   return self.saldo
    # elif valor<0:
    #   self.saldo-=valor
    #   return self.saldo
    # else:
    #   return f'Não teve alteração do saldo'
      