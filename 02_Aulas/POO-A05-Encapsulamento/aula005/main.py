#main 

from classes.classe import Conta

c1=Conta("João",20)
# c1.set_alterar_saldo=-50
# c1._Conta__saldo=2000
saida=c1.get_mostrar_saldo
# print(f'{c1.get_mostrar_saldo}')
print(saida)