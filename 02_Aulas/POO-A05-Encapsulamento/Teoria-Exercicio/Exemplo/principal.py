from classes.cl import Conta

c1=Conta('Richard',50)
print(c1)
c1.get_mostrar_saldo
c1.set_alterar_saldo=+20
c1.set_alterar_saldo=-100
c1._Conta__saldo=100000
print(c1.get_mostrar_saldo)