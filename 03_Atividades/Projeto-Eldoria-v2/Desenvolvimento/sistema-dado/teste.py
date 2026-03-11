# from random import randint

# var = randint(0, 10)
# while True:
#     num = int(input("Digite um numero: "))
#     if num > var:
#         print("Numero muito alto!")
#     elif num < var:
#         print("Numero baixo!")
#     else:
#         print('Você acertou!')
#         sair = str(input('Quer continuar? s/n'))
#         if sair in 'SsNn':
#             var = randint(0, 10)
#             if sair in 'Nn':
#                 break
#         else:
#             print('Erro valor invalido, tente novamente!')

from dados import SistemaDeDados

var = SistemaDeDados.rolar_d20()
print(var)
