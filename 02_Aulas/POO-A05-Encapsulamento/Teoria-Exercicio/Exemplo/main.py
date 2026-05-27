from classes.Classes import Conta
c1=Conta('Professor',200)
# # print(c1)
# # print(c1.monstar_saldo())
# c2=c1.monstar_saldo()
# print(c2)
print(f'Saldo atual R${c1.mostar_saldo}')
c1.alterar_saldo=500
c1.mostar_saldo= 600
c1._Conta__saldo=1000000
print(f'Saldo atual R${c1.mostar_saldo}')
