# Teoria de estruturas aninhadas

# 1. DICIONÁRIO DENTRO DE DICIONÁRIO

    dicionario["chave"]["sub_chave"] → acessa valor aninhado
    dicionario["chave"]["sub_chave"] = valor → altera valor aninhado

# Dicionário dentro de dicionário

```python

empresa = {
"nome": "AEMS",
"endereco": {
"cidade": "Três Lagoas",
"estado": "MS",
"cep": "12345-678"
}
}
```

# Acessando valor aninhado

    print(empresa["nome"])
    print(empresa["endereco"]["cidade"])
    print(empresa["endereco"]["estado"])

# Alterando valor aninhado

empresa["endereco"]["cidade"] = "Campo Grande"

# Adicionando nova sub-chave

empresa["endereco"]["pais"] = "Brasil"

# Percorrendo o dicionário externo

```python
for chave, valor in empresa.items():
print(f'{chave}: {valor}')
```

# Percorrendo inclusive o dicionário interno

```python
for chave, valor in empresa.items():
    if isinstance(valor, dict):
        print(f'{chave}:')
        for sub_chave, sub_valor in valor.items():
            print(f' {sub_chave}: {sub_valor}')
    else:
        print(f'{chave}: {valor}')
print(empresa)
```

# 2. LISTA DENTRO DE DICIONÁRIO

    dicionario["chave"][indice] → acessa item da lista interna
    dicionario["chave"].append() → adiciona item na lista interna

```python
aluno = {
"nome": "Richard",
"notas": [7.5, 8.0, 9.0],
"cursos": ["Python", "SQL", "Excel"]
}
```

# Acessando a lista interna

    print(aluno["notas"]) # [7.5, 8.0, 9.0]
    print(aluno["notas"][0]) # 7.5 → primeiro elemento
    print(aluno["cursos"][-1]) # Excel → último elemento

# Adicionando item na lista interna

    aluno["notas"].append(10.0)
    aluno["cursos"].append("Power BI")

# Alterando item da lista interna

    aluno["notas"][0] = 8.5

# Calculando média das notas

    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f'Média: {media:.2f}')

# Percorrendo a lista interna

    for nota in aluno["notas"]:
    print(nota)

    for curso in aluno["cursos"]:
    print(curso)

    print(aluno)

# 3. DICIONÁRIO DENTRO DE LISTA

    lista[indice]["chave"] → acessa valor do dicionário pelo índice

# for item in lista → percorre cada dicionário da lista

```python
produtos = [
{"nome": "Notebook", "preco": 1500.00, "quantidade": 5},
{"nome": "Cadeira", "preco": 350.00, "quantidade": 12},
{"nome": "Headset", "preco": 200.00, "quantidade": 0},
]
```

# Acessando pelo índice da lista

    print(produtos[0]) # dicionário inteiro
    print(produtos[0]["nome"]) # Notebook
    print(produtos[1]["preco"]) # 350.0

# Adicionando novo dicionário na lista

    produtos.append({"nome": "Mouse", "preco": 80.00, "quantidade": 20})

# Alterando valor de um dicionário dentro da lista

    produtos[0]["quantidade"] = 10

# Percorrendo todos os dicionários

    for produto in produtos:
    print(produto["nome"], produto["preco"])

# Filtrando por condição

    for produto in produtos:
    if produto["quantidade"] > 0:
    print(f'{produto["nome"]} disponível')

# Encontrando o mais caro com max() e lambda

    mais_caro = max(produtos, key=lambda x: x["preco"])
    print(f'Mais caro: {mais_caro["nome"]} - R$ {mais_caro["preco"]}')

# Calculando valor total de todo o estoque

    total = sum(p["preco"] \* p["quantidade"] for p in produtos)
    print(f'Total em estoque: R$ {total}')

    print(produtos)
