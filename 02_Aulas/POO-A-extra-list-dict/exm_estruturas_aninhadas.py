import os
os.system("cls")
# Estruturas aninhadas

empresa = {
    "nome": "AEMS",
    "endereco": {
        "cidade": "Tres Lagoas",
        "estado": "MS"
    }
}

# print(empresa)
print(empresa['nome'])
print(empresa['endereco'])
print(empresa['endereco']['estado'])

empresa['nome'] = "Google"
print(empresa)

for k, v in empresa.items():
    print(k, v)

for k, v in empresa.items():
    if isinstance(v, dict):
        for key, value in v.items():
            print(key, value)
    else:
        print(k, v)

os.system("cls")

#  DICIONARIO/LISTA

alunos = {
    'nome': 'Richard',
    'notas': [10, 8, 9],
}

print(alunos)
disciplinas = ['Front', 'Back', 'Dados']
alunos['disciplinas'] = disciplinas
print(alunos)
print(alunos['nome'])
print(alunos['disciplinas'][1])
alunos['nome'] = 'Joao'
print(alunos['nome'])
alunos['disciplinas'][0] = 'Java'
print(alunos['disciplinas'])
os.system('cls')
# Lista / Discionario
mercado = [
    {'item': 'pao',
     'preco': 10

     },
    {'item': 'arroz',
     'preco': 25

     }
]
print(mercado)
print(mercado[1])
print(mercado[1]['preco'])
