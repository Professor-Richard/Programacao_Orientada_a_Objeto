import os
# Exemplo Dicionario
dicionario = {}
# dicionario = {"chave": "Valor"}
dicionario = {'nome': 'aluno', 'nota': 3, "situacao": True}

print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

# Percorrer o dicionario

for chave in dicionario:
    print(chave)

for chave, valor in dicionario.items():
    print(chave, valor)

dicionario['situacao'] = False
print(dicionario)

dicionario['cidade'] = "Tres Lagoas"
print(dicionario)
os.system('cls')

dicionario = {"nome": input("Nome:"), "idade": input('Idade')}
print(dicionario)
