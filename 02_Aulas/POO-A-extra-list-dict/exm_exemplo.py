import os
from random import randint
# # Tupla ()
# # lista []
# # Dicionario{}

# # -- Dicionario--
# # Chave/ VALOR
# os.system('cls')
# # ataque/defesa/vida
# inimigos = {
#     1: ["goblin", 21, 20, 30],
#     2: ["lobo", 30, 26, 12],
#     3: ["aranha", 40, 26, 12],

# }
# # print(inimigos)
# var = randint(1, 3)
# var2 = randint(1, 3)

# # print(
# #     f'Inimigo:{inimigos[var][0]}, Ataque: {inimigos[var][1]}, defesa: {inimigos[var][2]}')
# print(f'Batalha de {inimigos[var][0]} x {inimigos[var2][0]}')
# dano = inimigos[var][1] - inimigos[var2][2]
# if dano > 0:
#     inimigos[var2][3] = dano
#     print(f'Tomou um dano de {dano}')
#     print(
#         f'Inimigo {inimigos[var2][0]} ficou com {inimigos[var2][3]} pontos de vida')


# DICT/DICT
os.system("cls")
inimigo = {
    "inimigo1": {
        "ataque": 20,
        "defesa": 30
    },
    "inimigo2": {
        "ataque": 10,
        "defesa": 40
    }
}
print(inimigo["inimigo1"]['ataque'])
print(inimigo["inimigo2"]['defesa'])
